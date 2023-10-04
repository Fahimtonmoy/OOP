from bank_acc import *
import pickle

acc_dict = {}

def make_account(amount, name, function):
    acc = function(amount, name)
    acc_dict[acc.name] = acc

                 
                 
make_account(1000, 'fahim', BankAccount)
make_account(2000, 'muhtasim', interestReward)
make_account(3000, 'hossain', ServiceCharge)

acc_dict["fahim"].deposit(1000)
acc_dict["muhtasim"].deposit(500)
acc_dict["hossain"].withdraw(2050)

acc_dict['hossain'].money_transfer(1000, acc_dict['muhtasim'])
acc_dict['fahim'].money_transfer(2010, acc_dict['hossain'])


def save_object(file, objs):
    with open(file, 'wb') as f:
        for obj in objs:
            pickle.dump(obj, f)
        f.close()
        

def load_object(file):
    objs = []
    with open(file, 'rb') as f:
        while True:
            try:
                obj = pickle.load(f)
                objs.append(obj)
            except EOFError:
                break
        f.close()
        return objs

filename = 'objects.pkl'
save_object(filename, [acc_dict['fahim'], acc_dict['muhtasim'], acc_dict['hossain']])


objects = load_object('objects.pkl')

def object_info(obj):
    print("#" * 20)
    for index, x in enumerate(obj):
        print(f"account {index+1} name: {x.name} \nBalance: {x.balance}")

object_info(objects)
print(len(objects))


for i in range(len(objects)):
    objects[i].deposit(1000)

save_object(filename, objects)

objects = load_object('objects.pkl')
object_info(objects)




