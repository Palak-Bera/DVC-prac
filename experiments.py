import mlflow

def calc(a , b , operation=None):
    if operation == "add":
        return (a+b)
    if operation == "mul":
        return (a*b)
    if operation == "div":
        return (a/b)
    if operation == "sub":
        return (a-b)
    
if __name__ == "__main__":
    a , b , opt =  10 , 20000 , "mul"
    with mlflow.start_run():
        result =  calc(a ,b , opt)
        mlflow.log_param('a', a)
        mlflow.log_param('b', b)
        mlflow.log_param('operation', opt)
        mlflow.log_param('result', result)
        print(f"result is {result}")
    