import time

class LcdApi:
    """
    This class provides a high-level API for communicating with HD44780-compatible LCD displays.
    It defines standard commands and methods for cursor movement, display control, and data writing.
    Low-level hardware access must be implemented in a subclass using the hal_* methods.
    """

    # LCD command set (based on HD44780 datasheet)
    LCD_CLR             = 0x01  # Clear display
    LCD_HOME            = 0x02  # Return cursor to home position

    LCD_ENTRY_MODE      = 0x04  # Set entry mode
    LCD_ENTRY_INC       = 0x02  # Cursor increment
    LCD_ENTRY_SHIFT     = 0x01  # Display shift

    LCD_ON_CTRL         = 0x08  # Display on/off control
    LCD_ON_DISPLAY      = 0x04  # Display on
    LCD_ON_CURSOR       = 0x02  # Cursor on
    LCD_ON_BLINK        = 0x01  # Cursor blink

    LCD_MOVE            = 0x10  # Cursor/display shift
    LCD_MOVE_DISP       = 0x08  # Display shift (0 = cursor)
    LCD_MOVE_RIGHT      = 0x04  # Shift right (0 = left)

    LCD_FUNCTION        = 0x20  # Function set
    LCD_FUNCTION_8BIT   = 0x10  # 8-bit mode (0 = 4-bit)
    LCD_FUNCTION_2LINES = 0x08  # Two-line display (0 = one-line)
    LCD_FUNCTION_10DOTS = 0x04  # 5x10 dots (0 = 5x7)
    LCD_FUNCTION_RESET  = 0x30  # Reset sequence

    LCD_CGRAM           = 0x40  # Set CGRAM address
    LCD_DDRAM           = 0x80  # Set DDRAM address

    LCD_RS_CMD          = 0
    LCD_RS_DATA         = 1

    LCD_RW_WRITE        = 0
    LCD_RW_READ         = 1

    def __init__(self, num_lines, num_columns):
        self.num_lines = min(num_lines, 4)
        self.num_columns = min(num_columns, 40)
        self.cursor_x = 0
        self.cursor_y = 0
        self.implied_newline = False
        self.backlight = True

        # Initialize display
        self.display_off()
        self.backlight_on()
        self.clear()
        self.hal_write_command(self.LCD_ENTRY_MODE | self.LCD_ENTRY_INC)
        self.hide_cursor()
        self.display_on()

    def clear(self):
        """Clear the LCD and reset the cursor to the top-left."""
        self.hal_write_command(self.LCD_CLR)
        self.hal_write_command(self.LCD_HOME)
        self.cursor_x = 0
        self.cursor_y = 0

    def show_cursor(self):
        """Show the cursor."""
        self.hal_write_command(self.LCD_ON_CTRL | self.LCD_ON_DISPLAY | self.LCD_ON_CURSOR)

    def hide_cursor(self):
        """Hide the cursor."""
        self.hal_write_command(self.LCD_ON_CTRL | self.LCD_ON_DISPLAY)

    def blink_cursor_on(self):
        """Enable blinking cursor."""
        self.hal_write_command(self.LCD_ON_CTRL | self.LCD_ON_DISPLAY |
                               self.LCD_ON_CURSOR | self.LCD_ON_BLINK)

    def blink_cursor_off(self):
        """Disable blinking, but keep cursor visible."""
        self.hal_write_command(self.LCD_ON_CTRL | self.LCD_ON_DISPLAY | self.LCD_ON_CURSOR)

    def display_on(self):
        """Turn on the LCD display."""
        self.hal_write_command(self.LCD_ON_CTRL | self.LCD_ON_DISPLAY)

    def display_off(self):
        """Turn off the LCD display."""
        self.hal_write_command(self.LCD_ON_CTRL)

    def backlight_on(self):
        """Turn on the LCD backlight (if supported)."""
        self.backlight = True
        self.hal_backlight_on()

    def backlight_off(self):
        """Turn off the LCD backlight (if supported)."""
        self.backlight = False
        self.hal_backlight_off()

    def move_to(self, cursor_x, cursor_y):
        """Move the cursor to a specified (x, y) position."""
        self.cursor_x = cursor_x
        self.cursor_y = cursor_y
        addr = cursor_x & 0x3F
        if cursor_y & 1:
            addr += 0x40
        if cursor_y & 2:
            addr += self.num_columns
        self.hal_write_command(self.LCD_DDRAM | addr)

    def putchar(self, char):
        """Write a single character to the LCD."""
        if char == '\n':
            if not self.implied_newline:
                self.cursor_x = self.num_columns
        else:
            self.hal_write_data(ord(char))
            self.cursor_x += 1

        if self.cursor_x >= self.num_columns:
            self.cursor_x = 0
            self.cursor_y += 1
            self.implied_newline = (char != '\n')

        if self.cursor_y >= self.num_lines:
            self.cursor_y = 0

        self.move_to(self.cursor_x, self.cursor_y)

    def putstr(self, string):
        """Write a string to the LCD."""
        for char in string:
            self.putchar(char)

    def custom_char(self, location, charmap):
        """
        Create a custom character.
        :param location: CGRAM location (0–7)
        :param charmap: List of 8 bytes defining the character (5x8 pixels)
        """
        location &= 0x07
        self.hal_write_command(self.LCD_CGRAM | (location << 3))
        self.hal_sleep_us(40)
        for i in range(8):
            self.hal_write_data(charmap[i])
            self.hal_sleep_us(40)
        self.move_to(self.cursor_x, self.cursor_y)

    # HAL methods (must be implemented in subclass)

    def hal_backlight_on(self):
        """Subclass should implement this to enable backlight control."""
        pass

    def hal_backlight_off(self):
        """Subclass should implement this to disable backlight control."""
        pass

    def hal_write_command(self, cmd):
        """Subclass must implement sending command to the LCD."""
        raise NotImplementedError

    def hal_write_data(self, data):
        """Subclass must implement sending data to the LCD."""
        raise NotImplementedError

    def hal_sleep_us(self, usecs):
        """Wait for a specified number of microseconds."""
        time.sleep_us(usecs)