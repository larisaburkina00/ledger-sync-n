# NFTDropSniper

**NFTDropSniper** — инструмент для отслеживания новых минтов NFT в реальном времени. Полезен для мониторинга коллекций, дропов и активности контракта.

## 🚀 Что делает

- Подключается к Ethereum через Infura
- Следит за событием Transfer (mint)
- Показывает новые NFT, отчеканенные в контракте

## ⚙️ Настройка

1. Получите ключ Infura: https://infura.io
2. Укажите адрес NFT-контракта
3. Создайте `.env`:

```
INFURA_URL=https://mainnet.infura.io/v3/YOUR_INFURA_KEY
CONTRACT_ADDRESS=0x...
```

## ▶️ Запуск

```
pip install -r requirements.txt
python nft_drop_sniper.py
```

## 💡 Применение

- Мониторинг дропов и первичных минтов
- Отслеживание активности коллекции
- Сигналы для ботов или Telegram

## 🛡 Ограничение

Работает с контрактами, которые используют стандартные Transfer события.

## 📜 License

MIT
