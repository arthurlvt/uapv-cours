import utime
import gc
from machine import I2C
from lcd_api import LcdApi

# Constantes pour les broches du PCF8574
MASK_RS = 0x01       # P0 - Register Select
MASK_RW = 0x02       # P1 - Read/Write (toujours en écriture ici)
MASK_E  = 0x04       # P2 - Enable

SHIFT_BACKLIGHT = 3  # P3 - rétroéclairage
SHIFT_DATA      = 4  # P4 à P7 - données en 4 bits

class I2cLcd(LcdApi):
    """
    Classe dérivée de LcdApi pour contrôler un écran LCD HD44780 via un port I2C
    en utilisant une puce d'extension PCF8574.
    """

    def __init__(self, i2c, i2c_addr, num_lines, num_columns):
        """
        Initialise la connexion I2C avec l'écran LCD.
        Envoie les commandes nécessaires pour configurer l'écran en mode 4 bits.
        """
        self.i2c = i2c
        self.i2c_addr = i2c_addr

        # Mise à zéro initiale
        self.i2c.writeto(self.i2c_addr, bytes([0]))
        utime.sleep_ms(20)  # Attente pour que l'écran soit prêt

        # Séquence de réinitialisation (3 fois)
        self.hal_write_init_nibble(self.LCD_FUNCTION_RESET)
        utime.sleep_ms(5)
        self.hal_write_init_nibble(self.LCD_FUNCTION_RESET)
        utime.sleep_ms(1)
        self.hal_write_init_nibble(self.LCD_FUNCTION_RESET)
        utime.sleep_ms(1)

        # Passage en mode 4 bits
        self.hal_write_init_nibble(self.LCD_FUNCTION)
        utime.sleep_ms(1)

        # Appel au constructeur de la classe mère
        LcdApi.__init__(self, num_lines, num_columns)

        # Configuration du nombre de lignes
        cmd = self.LCD_FUNCTION
        if num_lines > 1:
            cmd |= self.LCD_FUNCTION_2LINES
        self.hal_write_command(cmd)

        gc.collect()

    def hal_write_init_nibble(self, nibble):
        """
        Écrit un demi-octet (4 bits) pour l'initialisation.
        Spécifique à la séquence d'initialisation.
        """
        byte = ((nibble >> 4) & 0x0F) << SHIFT_DATA
        self.i2c.writeto(self.i2c_addr, bytes([byte | MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytes([byte]))
        gc.collect()

    def hal_backlight_on(self):
        """
        Allume le rétroéclairage de l'écran LCD.
        """
        self.i2c.writeto(self.i2c_addr, bytes([1 << SHIFT_BACKLIGHT]))
        gc.collect()

    def hal_backlight_off(self):
        """
        Éteint le rétroéclairage de l'écran LCD.
        """
        self.i2c.writeto(self.i2c_addr, bytes([0]))
        gc.collect()

    def hal_write_command(self, cmd):
        """
        Envoie une commande à l'écran LCD.
        Les données sont transmises en deux parties (4 bits chacune).
        """
        # Partie haute du byte
        byte = ((self.backlight << SHIFT_BACKLIGHT) |
                (((cmd >> 4) & 0x0F) << SHIFT_DATA))
        self.i2c.writeto(self.i2c_addr, bytes([byte | MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytes([byte]))

        # Partie basse du byte
        byte = ((self.backlight << SHIFT_BACKLIGHT) |
                ((cmd & 0x0F) << SHIFT_DATA))
        self.i2c.writeto(self.i2c_addr, bytes([byte | MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytes([byte]))

        # Délai nécessaire pour certaines commandes (clear/home)
        if cmd <= 3:
            utime.sleep_ms(5)

        gc.collect()

    def hal_write_data(self, data):
        """
        Écrit un caractère (donnée) à afficher sur l'écran.
        Utilise également deux transferts de 4 bits.
        """
        # Partie haute du caractère
        byte = (MASK_RS |
                (self.backlight << SHIFT_BACKLIGHT) |
                (((data >> 4) & 0x0F) << SHIFT_DATA))
        self.i2c.writeto(self.i2c_addr, bytes([byte | MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytes([byte]))

        # Partie basse du caractère
        byte = (MASK_RS |
                (self.backlight << SHIFT_BACKLIGHT) |
                ((data & 0x0F) << SHIFT_DATA))
        self.i2c.writeto(self.i2c_addr, bytes([byte | MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytes([byte]))

        gc.collect()
