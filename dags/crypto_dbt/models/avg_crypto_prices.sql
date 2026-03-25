select
    cryptocurrency,
    AVG(current_price_usd) as average_price

from {{ ref('stg_crypto_prices') }}

group by cryptocurrency