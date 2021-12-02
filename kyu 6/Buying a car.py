def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    time_to_buy = startPriceOld + savingperMonth
    step = 0
    step_price = startPriceNew
    while time_to_buy < step_price:
        time_to_buy = startPriceOld * percentLossByMonth + savingperMonth
        step_price += startPriceNew * percentLossByMonth
        percentLossByMonth += 0.5
        step += 1

    print([step,time_to_buy - step_price])

nbMonths(2000, 8000, 1000, 1.5)