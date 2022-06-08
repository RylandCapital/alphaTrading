import momo.scorer as scorer
import momo.collector as collector


# this function uses the the account equity and or positions in the kucoin
# futures account to rebalance to the momentum model 
def rebalance():

    scores = scorer.scorer()
    live_model_allocation = scores['model']

    account_report = collector.account_report()
    



