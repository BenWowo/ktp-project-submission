import api_consumer
import db_writer

if __name__ == "__main__":
    # super good OOP naming 
    api_consumer.api_consumer().consume()

    print('This is db writer')
    db_writer.db_writer().write_csv("data.csv")
    print('db writer done')