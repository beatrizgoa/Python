
def removeOutliers(data):
    # Remove outliers in function of the click count
    data = data[data.click_count < 1000]
    return data
