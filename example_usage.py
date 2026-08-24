from client import C2cInstantResaleAiPricingShippingLabelClient

def main():
    client = C2cInstantResaleAiPricingShippingLabelClient()
    res = client.list_preloved_item_with_ai('Nintendo Switch OLED Console', 5)
    print('Listing: ' + res['listing_id'] + ' | Suggested Price: JPY ' + str(res['suggested_instant_sell_price_jpy']))
    print('24h Sale Probability: ' + str(res['estimated_sale_probability_within_24h_pct']) + '% | QR Label: ' + res['prepaid_qr_shipping_label_code'])
    print('Anonymous Shipping: ' + res['anonymous_p2p_shipping_carrier'] + ' | Escrow: ' + str(res['marketplace_protection_escrow_active']))

if __name__ == '__main__':
    main()
