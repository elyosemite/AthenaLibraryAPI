class TestDatabaseLocal:
    def test_main(self):
        metadata.create_all(engine)
        insert_user("Yuri", "Melo")
        print(select_user("Yuri"))
        connection.close()