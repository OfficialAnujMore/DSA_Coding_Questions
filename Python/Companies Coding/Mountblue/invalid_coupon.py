from collections import Counter


def invalid_coupon(n, arr):

    distinct_flag = True
    valid_coupons = [10, 20, 50, 100, 200, 500, 1000]
    sum = 0
    for i in range(0, n):
        
        if len(arr[i]) in range(10, 13):
            coupon = arr[i]
            alpha = coupon[0:3]
            alpha_count = 0
            if coupon[-1].isupper():
                for j in range(0, len(alpha)):
                    freq = Counter(alpha)
                    freq_count = 0
                    for k in freq:
                        if freq[k] == 1:
                            freq_count += 1
                        else:
                            # j = len(alpha)+1
                            break
                    if freq_count == 3:
                        if alpha[j].isupper():
                            alpha_count += 1

                    # print(alpha_count)
                    # if alpha[j].isupper() and distinct_flag == True:
                    #     for k in freq:
                    #         if freq[k]==1:

                    #            distinct_flag = True
                    #            alpha_count+=1
                    #         else:
                    #             j = len(alpha)
                    #             distinct_flag = False
                    #             break

                if alpha_count == 3:
                    years = coupon[3:7]
                    if len(years) == 4 and int(years) in range(1900, 2020):
                        if len(coupon) == 10:

                            discount_coupons = coupon[7:9]
                            if int(discount_coupons) in valid_coupons:
                                sum+=int(discount_coupons)
                        elif len(coupon) == 11:
                            discount_coupons = coupon[7:10]
                            if int(discount_coupons) in valid_coupons:
                                sum+=int(discount_coupons)
                        elif len(coupon) == 12:
                            discount_coupons = coupon[7:11]
                            if int(discount_coupons) in valid_coupons:
                                sum+=int(discount_coupons)
                        # print(years)
                    # print(alpha)

    return sum


# arr = ['A201550B', 'ABB19991000Z', 'XYZ200019Z', 'ERF200220', 'SCD203010T']
arr = ['QDB2012R20B', 'RED190250E', 'RFV201111T', 'TYU20121000E', 'AAA198710B','AbC200010E']
n = len(arr)
print(invalid_coupon(n, arr))
