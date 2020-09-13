from flask import Flask , request , json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine,Table, Column, String, MetaData,Integer,ForeignKey,DateTime
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base  

app = Flask(__name__)

db =  create_engine('postgresql+pg8000://root:root@localhost:5432/varian?user=sanjeev&password=1234')  
base = declarative_base()
Session = sessionmaker(db)  
session = Session()
base.metadata.create_all(db)


class JSON(base):  
    __tablename__ = 'task_list'

    id = Column(Integer, primary_key=True, autoincrement=True)
    Agent_id = Column(String, nullable=False)
    Task_id = Column(String, nullable=False)
    Task_type = Column(String, nullable=False)
    Product_name = Column(String, nullable=False)
    Template_name = Column(String, nullable=False)
    Status = Column(String, nullable=False)

@app.route('/')
def get_status():
    get = session.query(JSON).all()
    results = [{
                "Agent_id": n.Agent_id,
                "Task_id": n.Task_id,
                "Task_type": n.Task_type,
                "Product_name": n.Product_name,
                "Template_name": n.Template_name,
                "Status": n.Status 
            } for n in get]

    return json.dumps(results)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9001)


