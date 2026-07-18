prices = [100, 250, 500]

gst_prices = map(lambda price: price * 1.13, prices)

print(list(gst_prices))