import pandas as pd


def read_dataset(file_name):
    data = pd.read_csv(file_name, sep='\t', nrows=2000)
    return data


def form_product_statistics_data(data):
    data_amount = len(data.index)
    review_ids, product_titles, review_bodies = data["review_id"].tolist(),\
                                                data["product_title"].tolist(),\
                                                data["review_body"].tolist()
    product_ids, star_ratings, review_dates = data["product_id"].tolist(),\
                                              data["star_rating"].tolist(),\
                                              data["review_date"].tolist()
    insert_data = [(review_ids[i],
                    product_ids[i],
                    product_titles[i],
                    star_ratings[i],
                    review_bodies[i],
                    review_dates[i]
                    ) for i in range(data_amount)]
    return insert_data


def form_customer_statistics_data(data):
    data_amount = len(data.index)
    review_ids, review_bodies = data["review_id"].tolist(), data["review_body"].tolist()
    customer_ids, verified_purchases, review_dates = data["customer_id"].tolist(), \
                                              data["verified_purchase"].tolist(), \
                                              data["review_date"].tolist()
    insert_data = [(review_ids[i],
                    customer_ids[i],
                    verified_purchases[i],
                    review_bodies[i],
                    review_dates[i]) for i in range(data_amount)]
    return insert_data


def form_haters_backers_data(data):
    data_amount = len(data.index)
    review_ids = data["review_id"].tolist()
    customer_ids, star_ratings, review_dates = data["customer_id"].tolist(), \
                                                     data["star_rating"].tolist(), \
                                                     data["review_date"].tolist()
    insert_data = [(review_ids[i], customer_ids[i], star_ratings[i], review_dates[i]) for i in range(data_amount)]
    return insert_data
