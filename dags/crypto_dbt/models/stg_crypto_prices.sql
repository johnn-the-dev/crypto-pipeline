select
    coin_name as cryptocurrency,
    price as current_price_usd,
    volume as trading_volume_24h_usd,
    cast(timestamp as timestamp) as recorded_at

from public.crypto_prices