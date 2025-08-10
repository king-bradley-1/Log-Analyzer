import logging
import random
from collections import Counter
from datetime import datetime, timedelta


def main():
    generate_logs()
    analyze_logs()


def generate_logs():
    logging.basicConfig(filename="app.log", format="%(levelname)s: %(message)s", filemode="a", level=logging.DEBUG)
    logger = logging.getLogger()
    logger.info("START")
    sample_messages = [
        "User login successful user_id={}",
        "User login failed for username={}",
        "Payment processed for order_id={}",
        "Failed to process transaction ID={}",
        "Item added to cart product_id={}",
        "Database connection timeout",
        "Cache refreshed for key={}",
        "Unexpected null value in field={}",
    ]
    levels = [logging.INFO, logging.WARNING, logging.DEBUG, logging.ERROR, logging.CRITICAL]
    usernames = ["alice", "bob", "charlie", "david"]
    product_ids = [101, 202, 303, 404]
    transaction_ids = [555, 666, 777, 888]
    order_ids = [12345, 67890, 24680]

    for i in range(10_000):
        value = random.choice(usernames + product_ids + transaction_ids + order_ids)
        message = random.choice(sample_messages).format(value)
        level = random.choice(levels)
        fake_time = datetime.now() - timedelta(days=random.randint(0, 30))
        timestamp = fake_time.strftime("%Y-%m-%d %H:%M:%S")
        file = f"file_{random.randint(1, 99)}"
        line = f"{timestamp}: {file}: {message}"
        logger.log(level, line)
    logger.info("FINISH")


def analyze_logs():
    errors, info, warn, debug, critical = 0, 0, 0, 0, 0
    data, messages = [], []
    with open("app.log") as f:
        for line in f:
            if "ERROR: " in line: errors += 1
            if "INFO: " in line: info += 1
            if "WARNING: " in line: warn += 1
            if "DEBUG: " in line: debug += 1
            if "CRITICAL: " in line: critical += 1
            messages.append(line.strip().split(": ")[-1])
    most_common_message, count = Counter(messages).most_common(1)[0]
    print(f"Total Lines: {errors + info + warn + debug + critical}")
    print(f"Errors: {errors}")
    print(f"Info: {info}")
    print(f"Warnings: {warn}")
    print(f"Debug: {debug}")
    print(f"Critical: {critical}")
    print(f"Most Common Error: '{most_common_message}' occurs {count} times")


if __name__ == "__main__":
    main()
