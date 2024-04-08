"""
This module simulates the returned data of the top most profitable traders on Solana
over different specified time periods. In future development, the backend infrastructure to acquire
this data natively can be built with the right resources.

This data can be gathered via the below methods, in order of descending complexity: 
A) Running a Solana Validator, taking a snapshot of all the transactions going through all major swap
platforms' (such as Raydium) AMM program address, and then aggregating the data by wallet to find the
desired statistics about each wallet. 

B) As in (A), but using existing blockchain explorer API's to gather the snapshot data, such as SolScan PRO or Birdeye PRO.

C) As in (A), but using an existing private RPC endpoint service to gather the snapshot data, such as,
Chainstack instead of running a full validator gathering the snapshot data.
"""
import requests

def return_api_data(time_period):
    return 0

data = {
    "24Hrs": {
        "E52Aoen8NNwYYauDT53ecuWPbabK8hsuLEijq5PUmihB": {"PnL": "+$1.54M", "Percentage Gain": "74%"},
        "E9P26d7LMeAUSFohkLUkQPr9Ww3J6A4qHJ3cQXbDKDia": {"PnL": "+$1.12M", "Percentage Gain": "99%"},
        "CJhpTiUXqcBJQZVr5TT6kyu8WXg6QdQuykfqygDyBtEB": {"PnL": "+$647.55K", "Percentage Gain": "5.8%"},
        "3cJ7izJHaRZKmN17oaQ1MCaKs379eGDaaLcDaRrf3Pbz": {"PnL": "+$384.67K", "Percentage Gain": "36.6%"},
        "benRLpbWCL8P8t51ufYt522419hGF5zif3CqgWGbEUm": {"PnL": "+$369.49K", "Percentage Gain": "1.5%"},
        "GRhwoZy8YSzfn8XUtTidztvKjMwoaYrgmjBbmeG62J55": {"PnL": "+$261.72K", "Percentage Gain": "432%"},
        "bobCPc5nqVoX7r8gKzCMPLrKjFidjnSCrAdcYGCH2Ye": {"PnL": "+$195.01K", "Percentage Gain": "0.9%"},
        "EiHtZuBtsSDzZrsKLGYvBsBnaiLJWZxwzVnSBpao5ReU": {"PnL": "+$188.32K", "Percentage Gain": "11546%"},
        "FC3nyVqdufVfrgXiRJEqgST1JdJSEBEz6a9KoBfFP7c4": {"PnL": "+$187.87K", "Percentage Gain": "673%"},
        "2LptbJWk1hwW9cZEnjGyM9YYxQP8XnnR2kBjMrtXZz4A": {"PnL": "+$187.66K", "Percentage Gain": "8222%"}
        },

    "3D": {
        "E52Aoen8NNwYYauDT53ecuWPbabK8hsuLEijq5PUmihB": {"PnL": "+$1.57M", "Percentage Gain": "78%"},
        "B2egtV7e7Bpr4F74fKLLABn3gxihuLYhqSPvcgD3VyLY": {"PnL": "+$417.96K", "Percentage Gain": "86%"},
        "BkeHJikPVN98j45cYp2S3N7s9qRm1fyFBRE2sRv6Xoja": {"PnL": "+$310.89K", "Percentage Gain": "95%"},
        "3cJ7izJHaRZKmN17oaQ1MCaKs379eGDaaLcDaRrf3Pbz": {"PnL": "+$275.39K", "Percentage Gain": "40%"},
        "9oTd6CjLufdADNLyvhde4meGGLdeBmao4pNVqmPoh9Wp": {"PnL": "+$205.16K", "Percentage Gain": "85%"},
        "NKEAA2dXBFbPSCGC2iAhFi8aaNG9yUbNDBGhUYqRBrb": {"PnL": "+$189.85K", "Percentage Gain": "84%"},
        "DecXrBS8ADaac7yqLcC6WxNNAfMhVsF1SHmvSNv66yDe": {"PnL": "+$189.64K", "Percentage Gain": "68%"},
        "KBFA4ziVawDBBRvtazBA5L7dDwuLS4NbGgPVcmpE4qD": {"PnL": "+$179.47K", "Percentage Gain": "552%"},
        "263MhtQnyoF7NEQt186GuhXhKKL2AAwD1c24CRT5cnav": {"PnL": "+$166.4K", "Percentage Gain": "115%"},
        "6T2jM4hKY2QZY1PYwAcMMuLgZt55rEHyYP4YqqHo8p37": {"PnL": "+$154.94K", "Percentage Gain": "80%"}
    },


    "1Week": {
        "E52Aoen8NNwYYauDT53ecuWPbabK8hsuLEijq5PUmihB": {"PnL": "+$7.17M", "Percentage Gain": "71.7%"},
        "GJ8KyJv3guyNZgf8EoEn4XoWJqAhAaPespN2BTJpGDy": {"PnL": "+$3.17M", "Percentage Gain": "43.6%"},
        "DcgVuxrYHCZQUtLgYSddqL12FKYa2qnWcGGyb1H79thc": {"PnL": "+$2.33M", "Percentage Gain": "20.4%"},
        "4BVu5pBC3cuS6CzpMvUdZ1VqDmuUJvNghHVLuA4TSSEE": {"PnL": "+$2.1M", "Percentage Gain": "22.1%"},
        "3cJ7izJHaRZKmN17oaQ1MCaKs379eGDaaLcDaRrf3Pbz": {"PnL": "+$2.06M", "Percentage Gain": "42.0%"},
        "Bq2RWav5LtfnAs8refzrYjfroDGK9vjYULmTqJX7yXfJ": {"PnL": "+$1.96M", "Percentage Gain": "12.3%"},
        "BitchYHrrCjDweArb8FKkPPYA1FniEsgTMJWPUjqbLq": {"PnL": "+$1.34M", "Percentage Gain": "10.8%"},
        "DkaA821Ptwfskum5Q3XfeES5TYcstaz4jqbyfwE5g3nS": {"PnL": "+$1.31M", "Percentage Gain": "1.06%"},
        "E9P26d7LMeAUSFohkLUkQPr9Ww3J6A4qHJ3cQXbDKDia": {"PnL": "+$1.12M", "Percentage Gain": "98.2%"},
        "8FMYC4XWAW2Ma3VSg5mmtNBcuzK9eLGKkwNVS5VqmpjV": {"PnL": "+$1.1M", "Percentage Gain": "95.7%"}
    },

    "1Month": {
        "EH1RFzxD7EvsuADcsvLzcmXCtT3MHg39JyjKmeVEhLWu": {"PnL": "+$18.19M", "Percentage Gain": "664%"},
        "DzssMBG83ySNoizUpGVLvKmvTtzGRf9KFwBQbE15nYcL": {"PnL": "+$15.01M", "Percentage Gain": "3275%"},
        "3PJkL127EtuoQucWK4gULWzzxEM25CgGGEF6r5Jx5xHs": {"PnL": "+$12.7M", "Percentage Gain": "18100%"},
        "B7JNMyQRymqurXntuEprz7BRpg2gAd6zsUBKEAkN8qbi": {"PnL": "+$12.35M", "Percentage Gain": "20583%"},
        "YtCeB2dzAWFCuxQtDRWup7LvCVHQDF7T2NDZtTdKrsG": {"PnL": "+$11.44M", "Percentage Gain": "3987%"},
        "71WDyyCsZwyEYDV91Qrb212rdg6woCHYQhFnmZUBxiJ6": {"PnL": "+$11.4M", "Percentage Gain": "0.3%"},
        "AupTbxArPau5H97izWurgska1hEvFNrYM1U8Yy9ijrWU": {"PnL": "+$10.94M", "Percentage Gain": "35.2%"},
        "4EHD5DMwsoXhGkP2tr43CWkVAXmjMDcWkpyaytgWrfpa": {"PnL": "+$9.92M", "Percentage Gain": "3645%"},
        "HoRmGrk35Uwb7UsRihctgBAbpvCjrPoCZurnsbTBiYpM": {"PnL": "+$9.36M", "Percentage Gain": "44200%"},
        "E52Aoen8NNwYYauDT53ecuWPbabK8hsuLEijq5PUmihB": {"PnL": "+$8.38M", "Percentage Gain": "70%"}
    }
}

