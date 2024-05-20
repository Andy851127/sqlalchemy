from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from typing import List
from sqlalchemy.orm.session import Session
import models
import database
import schemas

datadate = "20230803"
class CRUD:
    def __init__(self):
        self.SessionClass = sessionmaker(bind=database.engine)
        self.session = self.SessionClass()  # 創建會話
        

    def sql_select(self,table:str,condition:str = None) -> List:
        try:
            if condition:
                results = self.session.query(eval(table)).filter(eval(table).DATA_DATE == datadate,eval(condition)).all()
            else:
                results = self.session.query(eval(table)).filter(eval(table).DATA_DATE == datadate).all()
            
            data_lists = [obj.__dict__ for obj in results]
            for data_list in data_lists:
                data_list.pop('_sa_instance_state', None)
            return data_lists
        except Exception as e:
            print(e)
        finally:
            self.session.close()

    def sql_delete(self,table:str,condition:str = None) -> bool:
        try:
            print(f"self.session.query({eval(table)}).filter({eval(table)}.DATA_DATE == datadate,{eval(condition)}).delete()")
            if condition:
                self.session.query(eval(table)).filter(eval(table).DATA_DATE == datadate,eval(condition)).delete()
            else:
                self.session.query(eval(table)).filter(eval(table).DATA_DATE == datadate).delete()
            self.session.commit()  # 提交事務
            
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.session.close()

    def get_app_dtl_0card_elec(self):
        table = "models.AP_MDL_CCF_ACS_APP_DTL_0CARD_ELEC"
        return self.sql_select(table)
    
    def get_app_dtl_0card_norm(self):
        table = "models.AP_MDL_CCF_ACS_APP_DTL_0CARD_NORM"
        return self.sql_select(table)
    
    def get_ap_mdl_ad_bert(self):
        table = "models.AP_MDL_AD_BERT"
        condition = "and_(models.AP_MDL_AD_BERT.START_DT.isnot(None),models.AP_MDL_AD_BERT.BIRTHDAY != '00010101')"
        return self.sql_select(table,condition)

    def get_ap_mdl_ad_bert_null(self):
        table = "models.AP_MDL_AD_BERT"
        condition = "models.AP_MDL_AD_BERT.NEW_PROD_CATG_CD.is_(None)"
        return self.sql_select(table,condition)

    def get_ap_mdl_ad_feature_engineering(self):
        table = "models.AP_MDL_AD_FEATURE_ENGINEERING"
        condition = "models.AP_MDL_AD_FEATURE_ENGINEERING.START_DT.isnot(None)"
        return self.sql_select(table,condition)

    def delete_ap_mdl_ad_bert_null(self):
        table = "models.AP_MDL_AD_BERT"
        condition = "models.AP_MDL_AD_BERT.NEW_PROD_CATG_CD.is_(None)"
        return self.sql_delete(table,condition)

if __name__ == "__main__":
    crud = CRUD()
    result = crud.get_ap_mdl_ad_bert()
    print(result)