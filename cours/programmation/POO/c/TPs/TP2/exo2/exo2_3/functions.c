
float addMargin(float price) {
    price += price * 0.3;
    return price;
}

float addVAT(float price) {
    price += price * 0.2;
    return price;
}

float addEcoTax(float price) {
    price += 1.5;
    return price;
}

float getPriceWithTaxes(float price) {
    float newPrice = addMargin(price);
    float secondNewPrice = addVAT(newPrice);
    float thirdNewPrice = addEcoTax(secondNewPrice);
    return thirdNewPrice;
}