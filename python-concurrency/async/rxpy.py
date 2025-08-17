### reactive system programming ---> different from event driven programs
###                             ---> observing data more important, action only when certain condition achieved

from reactivex import Observable


anomaly_checks = [
    { 'INITL': 'GSE', 'VAL' : 200 },
    { 'INITL': 'TFARM', 'VAL' : 670 },
    { 'INITL': 'SHIP', 'VAL' : 220 },
    { 'INITL': 'BOOSTER', 'VAL' : 200 },
    { 'INITL': 'STACK', 'VAL' : 220 }
]

def go_launch(observer):
    for condition in anomaly_checks:
        if(condition['VAL'] > 190):
            observer.on_next(condition['INITL'])
        else:
            print("Ignore Item")
            break
    observer.on_completed()
