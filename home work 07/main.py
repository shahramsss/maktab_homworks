import my_test

test_account = my_test.Account("ali", 2000)
print(test_account.name)
print(test_account.min_remaining)

test_account.deposit(4000)
print("min reaming  : ", test_account.min_remaining)
