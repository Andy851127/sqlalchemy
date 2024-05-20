from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship
from database import Base

class AP_MDL_CCF_ACS_APP_DTL_0CARD(Base):
    __tablename__ = 'AP_MDL_CCF_ACS_APP_DTL_0CARD'  # 定义表名
    EDI_NO = Column(String(12))
    DATA_DATE = Column(String(8),index=True)
    MAJ_SEQ_ID = Column(Numeric(18,0), primary_key=True,index=True)
    APLY_TYPE_ID = Column(Numeric(18,0),index=True)
    APP_CASE_ID = Column(String(20))
    EP_CASE_ID = Column(String(20))
    EC_ORDER_ID = Column(String(50))
    MOTO_CASE_MAJ = Column(Numeric(18,0))
    QUICK_RESULT_CD = Column(String(30))
    OLD_APP_NO = Column(String(20))
    APP_NO = Column(String(20))
    INST_CD = Column(String(20))
    COMP_ID = Column(Numeric(18,0))
    CUST_ID = Column(String(10))
    CUST_NME = Column(String(100))
    ID_TYPE_ID = Column(Numeric(18,0))
    SEX = Column(Numeric(18,0))
    BUSN_TYPE_ID = Column(Numeric(18,0))
    VENDER_NO = Column(String(10))
    VENDER_NME = Column(String(120))
    VENDER_CLASS = Column(String(2))
    VENDER_ID2 = Column(String(40))
    VENDER_NME2 = Column(String(120))
    VENDER_CLASS2 = Column(String(2))
    VENDER_ID3 = Column(String(40))
    VENDER_NME3 = Column(String(50))
    VENDER_CLASS3 = Column(String(50))
    VNO2 = Column(String(40))
    IS_RAPID_SERVICE = Column(Numeric(18,0))
    CRD_REPLY_TIME = Column(Numeric(18,0))
    CRD_LIMIT = Column(Numeric(18,0))
    STATUS = Column(String(1))
    START_DT = Column(String(8))
    APLY_DT = Column(String(17))
    NOTICE_TIME = Column(String(17))
    NOTICE_DESC = Column(String(100))
    SECRET_FLAG = Column(Numeric(18,0))
    OBJ_TTL_AMT = Column(Numeric(18,0),index=True)
    OBJ_NME = Column(String(300))
    NOTICE_ITEM = Column(String(100))
    MOD_APP_RMK = Column(String(1000))
    BIRTHDAY = Column(String(8))
    MARRIAGE = Column(Numeric(18,0))
    DISABLE_CERT_IND = Column(Numeric(18,0))
    DISABLE_CERT_RMK = Column(String(8))
    ID_CARD_DATE = Column(String(8))
    ID_CARD_TYPE_ID = Column(Numeric(18,0))
    EDU_ID = Column(Numeric(18,0))
    HOUSE_TYPE_ID = Column(Numeric(18,0))
    MOBILE_1 = Column(String(20))
    MOBILE_2 = Column(String(20))
    EMAIL = Column(String(60))
    CITY_ID = Column(Numeric(18,0))
    REGION_ID = Column(Numeric(18,0))
    CUR_TEL = Column(String(30))
    REG_CITY_ID = Column(Numeric(18,0))
    REG_REGION_ID = Column(Numeric(18,0))
    REG_TEL = Column(String(20))
    RMK = Column(String(4000))    
    COMP_NME = Column(String(100))
    COMP_CITY_ID = Column(Numeric(18,0))
    COMP_REGION_ID = Column(Numeric(18,0))
    COMP_TEL = Column(String(30))  
    COMP_EXT = Column(String(10))  
    COMP_DEPT = Column(String(50))  
    JOB_TITLE = Column(String(50))
    SENIORITY = Column(Numeric(18,0))  
    SALARY = Column(Numeric(18,0))  
    PRD_NUM = Column(Numeric(18,0))  
    IS_NEW_CAR = Column(Numeric(18,0))
    ENG_NO = Column(String(30))
    ISSUE_DT = Column(String(8))
    LINC_NO = Column(String(20))
    MODEL = Column(String(50))
    RENEW_DT = Column(String(8))
    BRAND = Column(String(50))
    CC = Column(Numeric(18,3))
    PROD_YM = Column(String(6))
    CAR_YEARS = Column(Numeric(18,0))
    CRD_USR_ID = Column(String(20))
    CRD_USR_NME = Column(String(50))
    APPEAL_DT = Column(String(8))
    CUST_KIND_CD = Column(String(1))
    JOB_TITLE_ID = Column(Numeric(18,0))
    PROJ_REQ_TYPE_CD = Column(String(4))
    VIOLATE_REG_FLAG = Column(Numeric(18,0))
    PROD_CATG_CD = Column(String(4))
    CRD_WORKING_TIME = Column(Numeric(18,0))
    SECIAL_CASE_CD = Column(String(1))
    GUAR_BUY_BACK_ID = Column(Numeric(18,0))
    NEG_ITEM_IND = Column(Numeric(18,0))
    NEG_ITEM_ID = Column(String(50))
    APP_CRD_STATUS_CD = Column(String(1))
    APPEAL_REASON_TYPE_ID = Column(Numeric(18,0))
    APPEAL_RMK = Column(String(1000))
    CRD_LABER_INS_RESULT_ID = Column(Numeric(18,0))
    STUD_GOV_IND = Column(Numeric(18,0))
    LEHF_FLAG = Column(Numeric(18,0))
    APLY_FORM_TYPE_PROJ_ID = Column(String(30))
    FEE_TYPE_IND = Column(Numeric(18,0))
    ID_CARD_CITY_ID = Column(Numeric(18,0))
    TEL_MKT_IND = Column(Numeric(18,0))
    OTH_ZIP_CD = Column(String(5))
    OTH_CITY_ID = Column(Numeric(18,0))
    OTH_REGION_ID = Column(Numeric(18,0))
    OTH_ADDR = Column(String(200))
    LIMIT_BUY_COMMUN_PRD = Column(Numeric(18,0))
    IS_CO_MARKETING = Column(Numeric(18,0))
    FB_ACCT = Column(String(50))
    LINE_ACCT = Column(String(50))
    IG_ACCT = Column(String(50))
    LAST_COMP_NME = Column(String(100))
    LAST_COMP_DEPT = Column(String(50))
    LAST_JOB_TITLE = Column(String(50))
    PAY_TYPE_CD = Column(String(3))
    PAY_DAY = Column(Numeric(18,0))
    PAYEE_BNK_ID = Column(String(10))
    ORG_ONWR = Column(String(60))
    INSR_COMP = Column(String(60))
    EST_AMT = Column(Numeric(18,0))
    USE_YEAR = Column(Numeric(18,0))
    IS_PHONE_CASE = Column(Numeric(18,0))
    QUOTE_NME = Column(String(160))
    QUOTE_TYPE_NME = Column(String(200))
    SAL_DEPT_NME = Column(String(256))
    SAL_USR_NME = Column(String(50))
    APP_SAL_DEPT_NME = Column(String(256))
    APP_SAL_USR_NME = Column(String(50))
    APPEAL_USR_NME = Column(String(50))
    APPEAL_CRD_USR_NME = Column(String(50))
    GUAR_NME = Column(String(100))
    DATA_PREDICTION_RESULT_P = Column(String(10))
    DATA_PREDICTION_RESULT = Column(String(10))
    FACTORYSERVICE_USR_DEPT_NME = Column(String(256))
    FACTORYSERVICE_USR_NME = Column(String(50))
    MID_RETURN_CODE = Column(String(50))
    MID_RETURN_MSG = Column(String(500))
    PHONE_SALE_SRC_NME = Column(String(200))
    PHONE_SALE_SRC = Column(String(200))
    PHONE_PROD_CATG_NME = Column(String(200))
    CHANNEL_NME = Column(String(200))

class AP_MDL_CCF_ACS_APP_DTL_0CARD_NORM(Base):
    __tablename__ = 'AP_MDL_CCF_ACS_APP_DTL_0CARD_NORM'  # 定义表名
    EDI_NO = Column(String(12))
    DATA_DATE = Column(String(8),index=True)
    MAJ_SEQ_ID = Column(Numeric(18,0), primary_key=True,index=True)
    APLY_TYPE_ID = Column(Numeric(18,0),index=True)
    APP_CASE_ID = Column(String(20))
    EP_CASE_ID = Column(String(20))
    EC_ORDER_ID = Column(String(50))
    MOTO_CASE_MAJ = Column(Numeric(18,0))
    QUICK_RESULT_CD = Column(String(30))
    OLD_APP_NO = Column(String(20))
    APP_NO = Column(String(20))
    INST_CD = Column(String(20))
    COMP_ID = Column(Numeric(18,0))
    CUST_ID = Column(String(10))
    CUST_NME = Column(String(100))
    ID_TYPE_ID = Column(Numeric(18,0))
    SEX = Column(Numeric(18,0))
    BUSN_TYPE_ID = Column(Numeric(18,0))
    VENDER_NO = Column(String(10))
    VENDER_NME = Column(String(120))
    VENDER_CLASS = Column(String(2))
    VENDER_ID2 = Column(String(40))
    VENDER_NME2 = Column(String(120))
    VENDER_CLASS2 = Column(String(2))
    VENDER_ID3 = Column(String(40))
    VENDER_NME3 = Column(String(50))
    VENDER_CLASS3 = Column(String(50))
    VNO2 = Column(String(40))
    IS_RAPID_SERVICE = Column(Numeric(18,0))
    CRD_REPLY_TIME = Column(Numeric(18,0))
    CRD_LIMIT = Column(Numeric(18,0))
    STATUS = Column(String(1))
    START_DT = Column(String(8))
    APLY_DT = Column(String(17))
    NOTICE_TIME = Column(String(17))
    NOTICE_DESC = Column(String(100))
    SECRET_FLAG = Column(Numeric(18,0))
    OBJ_TTL_AMT = Column(Numeric(18,0),index=True)
    OBJ_NME = Column(String(300))
    NOTICE_ITEM = Column(String(100))
    MOD_APP_RMK = Column(String(1000))
    BIRTHDAY = Column(String(8))
    MARRIAGE = Column(Numeric(18,0))
    DISABLE_CERT_IND = Column(Numeric(18,0))
    DISABLE_CERT_RMK = Column(String(8))
    ID_CARD_DATE = Column(String(8))
    ID_CARD_TYPE_ID = Column(Numeric(18,0))
    EDU_ID = Column(Numeric(18,0))
    HOUSE_TYPE_ID = Column(Numeric(18,0))
    MOBILE_1 = Column(String(20))
    MOBILE_2 = Column(String(20))
    EMAIL = Column(String(60))
    CITY_ID = Column(Numeric(18,0))
    REGION_ID = Column(Numeric(18,0))
    CUR_TEL = Column(String(30))
    REG_CITY_ID = Column(Numeric(18,0))
    REG_REGION_ID = Column(Numeric(18,0))
    REG_TEL = Column(String(20))
    RMK = Column(String(4000))    
    COMP_NME = Column(String(100))
    COMP_CITY_ID = Column(Numeric(18,0))
    COMP_REGION_ID = Column(Numeric(18,0))
    COMP_TEL = Column(String(30))  
    COMP_EXT = Column(String(10))  
    COMP_DEPT = Column(String(50))  
    JOB_TITLE = Column(String(50))
    SENIORITY = Column(Numeric(18,0))  
    SALARY = Column(Numeric(18,0))  
    PRD_NUM = Column(Numeric(18,0))  
    IS_NEW_CAR = Column(Numeric(18,0))
    ENG_NO = Column(String(30))
    ISSUE_DT = Column(String(8))
    LINC_NO = Column(String(20))
    MODEL = Column(String(50))
    RENEW_DT = Column(String(8))
    BRAND = Column(String(50))
    CC = Column(Numeric(18,3))
    PROD_YM = Column(String(6))
    CAR_YEARS = Column(Numeric(18,0))
    CRD_USR_ID = Column(String(20))
    CRD_USR_NME = Column(String(50))
    APPEAL_DT = Column(String(8))
    CUST_KIND_CD = Column(String(1))
    JOB_TITLE_ID = Column(Numeric(18,0))
    PROJ_REQ_TYPE_CD = Column(String(4))
    VIOLATE_REG_FLAG = Column(Numeric(18,0))
    PROD_CATG_CD = Column(String(4))
    CRD_WORKING_TIME = Column(Numeric(18,0))
    SECIAL_CASE_CD = Column(String(1))
    GUAR_BUY_BACK_ID = Column(Numeric(18,0))
    NEG_ITEM_IND = Column(Numeric(18,0))
    NEG_ITEM_ID = Column(String(50))
    APP_CRD_STATUS_CD = Column(String(1))
    APPEAL_REASON_TYPE_ID = Column(Numeric(18,0))
    APPEAL_RMK = Column(String(1000))
    CRD_LABER_INS_RESULT_ID = Column(Numeric(18,0))
    STUD_GOV_IND = Column(Numeric(18,0))
    LEHF_FLAG = Column(Numeric(18,0))
    APLY_FORM_TYPE_PROJ_ID = Column(String(30))
    FEE_TYPE_IND = Column(Numeric(18,0))
    ID_CARD_CITY_ID = Column(Numeric(18,0))
    TEL_MKT_IND = Column(Numeric(18,0))
    OTH_ZIP_CD = Column(String(5))
    OTH_CITY_ID = Column(Numeric(18,0))
    OTH_REGION_ID = Column(Numeric(18,0))
    OTH_ADDR = Column(String(200))
    LIMIT_BUY_COMMUN_PRD = Column(Numeric(18,0))
    IS_CO_MARKETING = Column(Numeric(18,0))
    FB_ACCT = Column(String(50))
    LINE_ACCT = Column(String(50))
    IG_ACCT = Column(String(50))
    LAST_COMP_NME = Column(String(100))
    LAST_COMP_DEPT = Column(String(50))
    LAST_JOB_TITLE = Column(String(50))
    PAY_TYPE_CD = Column(String(3))
    PAY_DAY = Column(Numeric(18,0))
    PAYEE_BNK_ID = Column(String(10))
    ORG_ONWR = Column(String(60))
    INSR_COMP = Column(String(60))
    EST_AMT = Column(Numeric(18,0))
    USE_YEAR = Column(Numeric(18,0))
    IS_PHONE_CASE = Column(Numeric(18,0))
    QUOTE_NME = Column(String(160))
    QUOTE_TYPE_NME = Column(String(200))
    SAL_DEPT_NME = Column(String(256))
    SAL_USR_NME = Column(String(50))
    APP_SAL_DEPT_NME = Column(String(256))
    APP_SAL_USR_NME = Column(String(50))
    APPEAL_USR_NME = Column(String(50))
    APPEAL_CRD_USR_NME = Column(String(50))
    GUAR_NME = Column(String(100))
    DATA_PREDICTION_RESULT_P = Column(String(10))
    DATA_PREDICTION_RESULT = Column(String(10))
    FACTORYSERVICE_USR_DEPT_NME = Column(String(256))
    FACTORYSERVICE_USR_NME = Column(String(50))
    MID_RETURN_CODE = Column(String(50))
    MID_RETURN_MSG = Column(String(500))
    PHONE_SALE_SRC_NME = Column(String(200))
    PHONE_SALE_SRC = Column(String(200))
    PHONE_PROD_CATG_NME = Column(String(200))
    CHANNEL_NME = Column(String(200))

class AP_MDL_CCF_ACS_APP_DTL_0CARD_ELEC(Base):
    __tablename__ = 'AP_MDL_CCF_ACS_APP_DTL_0CARD_ELEC'  # 定义表名
    EDI_NO = Column(String(12))
    DATA_DATE = Column(String(8),index=True)
    MAJ_SEQ_ID = Column(Numeric(18,0), primary_key=True,index=True)
    APLY_TYPE_ID = Column(Numeric(18,0),index=True)
    APP_CASE_ID = Column(String(20))
    EP_CASE_ID = Column(String(20))
    EC_ORDER_ID = Column(String(50))
    MOTO_CASE_MAJ = Column(Numeric(18,0))
    QUICK_RESULT_CD = Column(String(30))
    OLD_APP_NO = Column(String(20))
    APP_NO = Column(String(20))
    INST_CD = Column(String(20))
    COMP_ID = Column(Numeric(18,0))
    CUST_ID = Column(String(10))
    CUST_NME = Column(String(100))
    ID_TYPE_ID = Column(Numeric(18,0))
    SEX = Column(Numeric(18,0))
    BUSN_TYPE_ID = Column(Numeric(18,0))
    VENDER_NO = Column(String(10))
    VENDER_NME = Column(String(120))
    VENDER_CLASS = Column(String(2))
    VENDER_ID2 = Column(String(40))
    VENDER_NME2 = Column(String(120))
    VENDER_CLASS2 = Column(String(2))
    VENDER_ID3 = Column(String(40))
    VENDER_NME3 = Column(String(50))
    VENDER_CLASS3 = Column(String(50))
    VNO2 = Column(String(40))
    IS_RAPID_SERVICE = Column(Numeric(18,0))
    CRD_REPLY_TIME = Column(Numeric(18,0))
    CRD_LIMIT = Column(Numeric(18,0))
    STATUS = Column(String(1))
    START_DT = Column(String(8))
    APLY_DT = Column(String(17))
    NOTICE_TIME = Column(String(17))
    NOTICE_DESC = Column(String(100))
    SECRET_FLAG = Column(Numeric(18,0))
    OBJ_TTL_AMT = Column(Numeric(18,0),index=True)
    OBJ_NME = Column(String(300))
    NOTICE_ITEM = Column(String(100))
    MOD_APP_RMK = Column(String(1000))
    BIRTHDAY = Column(String(8))
    MARRIAGE = Column(Numeric(18,0))
    DISABLE_CERT_IND = Column(Numeric(18,0))
    DISABLE_CERT_RMK = Column(String(8))
    ID_CARD_DATE = Column(String(8))
    ID_CARD_TYPE_ID = Column(Numeric(18,0))
    EDU_ID = Column(Numeric(18,0))
    HOUSE_TYPE_ID = Column(Numeric(18,0))
    MOBILE_1 = Column(String(20))
    MOBILE_2 = Column(String(20))
    EMAIL = Column(String(60))
    CITY_ID = Column(Numeric(18,0))
    REGION_ID = Column(Numeric(18,0))
    CUR_TEL = Column(String(30))
    REG_CITY_ID = Column(Numeric(18,0))
    REG_REGION_ID = Column(Numeric(18,0))
    REG_TEL = Column(String(20))
    RMK = Column(String(4000))    
    COMP_NME = Column(String(100))
    COMP_CITY_ID = Column(Numeric(18,0))
    COMP_REGION_ID = Column(Numeric(18,0))
    COMP_TEL = Column(String(30))  
    COMP_EXT = Column(String(10))  
    COMP_DEPT = Column(String(50))  
    JOB_TITLE = Column(String(50))
    SENIORITY = Column(Numeric(18,0))  
    SALARY = Column(Numeric(18,0))  
    PRD_NUM = Column(Numeric(18,0))  
    IS_NEW_CAR = Column(Numeric(18,0))
    ENG_NO = Column(String(30))
    ISSUE_DT = Column(String(8))
    LINC_NO = Column(String(20))
    MODEL = Column(String(50))
    RENEW_DT = Column(String(8))
    BRAND = Column(String(50))
    CC = Column(Numeric(18,3))
    PROD_YM = Column(String(6))
    CAR_YEARS = Column(Numeric(18,0))
    CRD_USR_ID = Column(String(20))
    CRD_USR_NME = Column(String(50))
    APPEAL_DT = Column(String(8))
    CUST_KIND_CD = Column(String(1))
    JOB_TITLE_ID = Column(Numeric(18,0))
    PROJ_REQ_TYPE_CD = Column(String(4))
    VIOLATE_REG_FLAG = Column(Numeric(18,0))
    PROD_CATG_CD = Column(String(4))
    CRD_WORKING_TIME = Column(Numeric(18,0))
    SECIAL_CASE_CD = Column(String(1))
    GUAR_BUY_BACK_ID = Column(Numeric(18,0))
    NEG_ITEM_IND = Column(Numeric(18,0))
    NEG_ITEM_ID = Column(String(50))
    APP_CRD_STATUS_CD = Column(String(1))
    APPEAL_REASON_TYPE_ID = Column(Numeric(18,0))
    APPEAL_RMK = Column(String(1000))
    CRD_LABER_INS_RESULT_ID = Column(Numeric(18,0))
    STUD_GOV_IND = Column(Numeric(18,0))
    LEHF_FLAG = Column(Numeric(18,0))
    APLY_FORM_TYPE_PROJ_ID = Column(String(30))
    FEE_TYPE_IND = Column(Numeric(18,0))
    ID_CARD_CITY_ID = Column(Numeric(18,0))
    TEL_MKT_IND = Column(Numeric(18,0))
    OTH_ZIP_CD = Column(String(5))
    OTH_CITY_ID = Column(Numeric(18,0))
    OTH_REGION_ID = Column(Numeric(18,0))
    OTH_ADDR = Column(String(200))
    LIMIT_BUY_COMMUN_PRD = Column(Numeric(18,0))
    IS_CO_MARKETING = Column(Numeric(18,0))
    FB_ACCT = Column(String(50))
    LINE_ACCT = Column(String(50))
    IG_ACCT = Column(String(50))
    LAST_COMP_NME = Column(String(100))
    LAST_COMP_DEPT = Column(String(50))
    LAST_JOB_TITLE = Column(String(50))
    PAY_TYPE_CD = Column(String(3))
    PAY_DAY = Column(Numeric(18,0))
    PAYEE_BNK_ID = Column(String(10))
    ORG_ONWR = Column(String(60))
    INSR_COMP = Column(String(60))
    EST_AMT = Column(Numeric(18,0))
    USE_YEAR = Column(Numeric(18,0))
    IS_PHONE_CASE = Column(Numeric(18,0))
    QUOTE_NME = Column(String(160))
    QUOTE_TYPE_NME = Column(String(200))
    SAL_DEPT_NME = Column(String(256))
    SAL_USR_NME = Column(String(50))
    APP_SAL_DEPT_NME = Column(String(256))
    APP_SAL_USR_NME = Column(String(50))
    APPEAL_USR_NME = Column(String(50))
    APPEAL_CRD_USR_NME = Column(String(50))
    GUAR_NME = Column(String(100))
    DATA_PREDICTION_RESULT_P = Column(String(10))
    DATA_PREDICTION_RESULT = Column(String(10))
    FACTORYSERVICE_USR_DEPT_NME = Column(String(256))
    FACTORYSERVICE_USR_NME = Column(String(50))
    MID_RETURN_CODE = Column(String(50))
    MID_RETURN_MSG = Column(String(500))
    PHONE_SALE_SRC_NME = Column(String(200))
    PHONE_SALE_SRC = Column(String(200))
    PHONE_PROD_CATG_NME = Column(String(200))
    CHANNEL_NME = Column(String(200))

class AP_MDL_AD_BERT(Base):
    __tablename__ = 'AP_MDL_AD_BERT'  # 定义表名
    EDI_NO = Column(String(12),index=True)
    DATA_DATE = Column(String(8),index=True)
    MAJ_SEQ_ID = Column(Numeric(18,0), primary_key=True,index=True)
    APLY_TYPE_ID = Column(Numeric(18,0))
    APP_CASE_ID = Column(String(20))
    EP_CASE_ID = Column(String(20))
    EC_ORDER_ID = Column(String(50))
    MOTO_CASE_MAJ = Column(Numeric(18,0))
    QUICK_RESULT_CD = Column(String(30))
    OLD_APP_NO = Column(String(20))
    APP_NO = Column(String(20))
    INST_CD = Column(String(20))
    COMP_ID = Column(Numeric(18,0))
    CUST_ID = Column(String(10))
    CUST_NME = Column(String(100))
    ID_TYPE_ID = Column(Numeric(18,0))
    SEX = Column(Numeric(18,0))
    BUSN_TYPE_ID = Column(Numeric(18,0))
    VENDER_NO = Column(String(10))
    VENDER_NME = Column(String(120))
    VENDER_CLASS = Column(String(2))
    VENDER_ID2 = Column(String(40))
    VENDER_NME2 = Column(String(120))
    VENDER_CLASS2 = Column(String(2))
    VENDER_ID3 = Column(String(40))
    VENDER_NME3 = Column(String(50))
    VENDER_CLASS3 = Column(String(50))
    VNO2 = Column(String(40))
    IS_RAPID_SERVICE = Column(Numeric(18,0))
    CRD_REPLY_TIME = Column(Numeric(18,0))
    CRD_LIMIT = Column(Numeric(18,0))
    STATUS = Column(String(1))
    START_DT = Column(String(8))
    APLY_DT = Column(String(17))
    NOTICE_TIME = Column(String(17))
    NOTICE_DESC = Column(String(100))
    SECRET_FLAG = Column(Numeric(18,0))
    OBJ_TTL_AMT = Column(Numeric(18,0))
    OBJ_NME = Column(String(300))
    NOTICE_ITEM = Column(String(100))
    MOD_APP_RMK = Column(String(1000))
    BIRTHDAY = Column(String(8))
    MARRIAGE = Column(Numeric(18,0))
    DISABLE_CERT_IND = Column(Numeric(18,0))
    DISABLE_CERT_RMK = Column(String(8))
    ID_CARD_DATE = Column(String(8))
    ID_CARD_TYPE_ID = Column(Numeric(18,0))
    EDU_ID = Column(Numeric(18,0))
    HOUSE_TYPE_ID = Column(Numeric(18,0))
    MOBILE_1 = Column(String(20))
    MOBILE_2 = Column(String(20))
    EMAIL = Column(String(60))
    CITY_ID = Column(Numeric(18,0))
    REGION_ID = Column(Numeric(18,0))
    CUR_TEL = Column(String(30))
    REG_CITY_ID = Column(Numeric(18,0))
    REG_REGION_ID = Column(Numeric(18,0))
    REG_TEL = Column(String(20))
    RMK = Column(String(4000))    
    COMP_NME = Column(String(100))
    COMP_CITY_ID = Column(Numeric(18,0))
    COMP_REGION_ID = Column(Numeric(18,0))
    COMP_TEL = Column(String(30))  
    COMP_EXT = Column(String(10))  
    COMP_DEPT = Column(String(50))  
    JOB_TITLE = Column(String(50))
    SENIORITY = Column(Numeric(18,0))  
    SALARY = Column(Numeric(18,0))  
    PRD_NUM = Column(Numeric(18,0))  
    IS_NEW_CAR = Column(Numeric(18,0))
    ENG_NO = Column(String(30))
    ISSUE_DT = Column(String(8))
    LINC_NO = Column(String(20))
    MODEL = Column(String(50))
    RENEW_DT = Column(String(8))
    BRAND = Column(String(50))
    CC = Column(Numeric(18,3))
    PROD_YM = Column(String(6))
    CAR_YEARS = Column(Numeric(18,0))
    CRD_USR_ID = Column(String(20))
    CRD_USR_NME = Column(String(50))
    APPEAL_DT = Column(String(8))
    CUST_KIND_CD = Column(String(1))
    JOB_TITLE_ID = Column(Numeric(18,0))
    PROJ_REQ_TYPE_CD = Column(String(4))
    VIOLATE_REG_FLAG = Column(Numeric(18,0))
    PROD_CATG_CD = Column(String(4))
    CRD_WORKING_TIME = Column(Numeric(18,0))
    SECIAL_CASE_CD = Column(String(1))
    GUAR_BUY_BACK_ID = Column(Numeric(18,0))
    NEG_ITEM_IND = Column(Numeric(18,0))
    NEG_ITEM_ID = Column(String(50))
    APP_CRD_STATUS_CD = Column(String(1))
    APPEAL_REASON_TYPE_ID = Column(Numeric(18,0))
    APPEAL_RMK = Column(String(1000))
    CRD_LABER_INS_RESULT_ID = Column(Numeric(18,0))
    STUD_GOV_IND = Column(Numeric(18,0))
    LEHF_FLAG = Column(Numeric(18,0))
    APLY_FORM_TYPE_PROJ_ID = Column(String(30))
    FEE_TYPE_IND = Column(Numeric(18,0))
    ID_CARD_CITY_ID = Column(Numeric(18,0))
    TEL_MKT_IND = Column(Numeric(18,0))
    OTH_ZIP_CD = Column(String(5))
    OTH_CITY_ID = Column(Numeric(18,0))
    OTH_REGION_ID = Column(Numeric(18,0))
    OTH_ADDR = Column(String(200))
    LIMIT_BUY_COMMUN_PRD = Column(Numeric(18,0))
    IS_CO_MARKETING = Column(Numeric(18,0))
    FB_ACCT = Column(String(50))
    LINE_ACCT = Column(String(50))
    IG_ACCT = Column(String(50))
    LAST_COMP_NME = Column(String(100))
    LAST_COMP_DEPT = Column(String(50))
    LAST_JOB_TITLE = Column(String(50))
    PAY_TYPE_CD = Column(String(3))
    PAY_DAY = Column(Numeric(18,0))
    PAYEE_BNK_ID = Column(String(10))
    ORG_ONWR = Column(String(60))
    INSR_COMP = Column(String(60))
    EST_AMT = Column(Numeric(18,0))
    USE_YEAR = Column(Numeric(18,0))
    IS_PHONE_CASE = Column(Numeric(18,0))
    QUOTE_NME = Column(String(160))
    QUOTE_TYPE_NME = Column(String(200))
    SAL_DEPT_NME = Column(String(256))
    SAL_USR_NME = Column(String(50))
    APP_SAL_DEPT_NME = Column(String(256))
    APP_SAL_USR_NME = Column(String(50))
    APPEAL_USR_NME = Column(String(50))
    APPEAL_CRD_USR_NME = Column(String(50))
    GUAR_NME = Column(String(100))
    DATA_PREDICTION_RESULT_P = Column(String(10))
    DATA_PREDICTION_RESULT = Column(String(10))
    FACTORYSERVICE_USR_DEPT_NME = Column(String(256))
    FACTORYSERVICE_USR_NME = Column(String(50))
    MID_RETURN_CODE = Column(String(50))
    MID_RETURN_MSG = Column(String(500))
    PHONE_SALE_SRC_NME = Column(String(200))
    PHONE_SALE_SRC = Column(String(200))
    PHONE_PROD_CATG_NME = Column(String(200))
    CHANNEL_NME = Column(String(200))
    NEW_PROD_CATG_CD = Column(String(4),index=True)
    DATA_SRC = Column(String(1),index=True)

class AP_MDL_AD_FEATURE_ENGINEERING(Base):
    __tablename__ = 'AP_MDL_AD_FEATURE_ENGINEERING'  # 定义表名
    EDI_NO = Column(String(12),index=True)
    DATA_DATE = Column(String(8),index=True)
    MAJ_SEQ_ID = Column(Numeric(18,0), primary_key=True,index=True)
    APLY_TYPE_ID = Column(Numeric(18,0))
    APP_CASE_ID = Column(String(20))
    EP_CASE_ID = Column(String(20))
    EC_ORDER_ID = Column(String(50))
    MOTO_CASE_MAJ = Column(Numeric(18,0))
    QUICK_RESULT_CD = Column(String(30))
    OLD_APP_NO = Column(String(20))
    APP_NO = Column(String(20))
    INST_CD = Column(String(20))
    COMP_ID = Column(Numeric(18,0))
    CUST_ID = Column(String(10))
    CUST_NME = Column(String(100))
    ID_TYPE_ID = Column(Numeric(18,0))
    SEX = Column(Numeric(18,0))
    BUSN_TYPE_ID = Column(Numeric(18,0))
    VENDER_NO = Column(String(10))
    VENDER_NME = Column(String(120))
    VENDER_CLASS = Column(String(2))
    VENDER_ID2 = Column(String(40))
    VENDER_NME2 = Column(String(120))
    VENDER_CLASS2 = Column(String(2))
    VENDER_ID3 = Column(String(40))
    VENDER_NME3 = Column(String(50))
    VENDER_CLASS3 = Column(String(50))
    VNO2 = Column(String(40))
    IS_RAPID_SERVICE = Column(Numeric(18,0))
    CRD_REPLY_TIME = Column(Numeric(18,0))
    CRD_LIMIT = Column(Numeric(18,0))
    STATUS = Column(String(1))
    START_DT = Column(String(8))
    APLY_DT = Column(String(17))
    NOTICE_TIME = Column(String(17))
    NOTICE_DESC = Column(String(100))
    SECRET_FLAG = Column(Numeric(18,0))
    OBJ_TTL_AMT = Column(Numeric(18,0))
    OBJ_NME = Column(String(300))
    NOTICE_ITEM = Column(String(100))
    MOD_APP_RMK = Column(String(1000))
    BIRTHDAY = Column(String(8))
    MARRIAGE = Column(Numeric(18,0))
    DISABLE_CERT_IND = Column(Numeric(18,0))
    DISABLE_CERT_RMK = Column(String(8))
    ID_CARD_DATE = Column(String(8))
    ID_CARD_TYPE_ID = Column(Numeric(18,0))
    EDU_ID = Column(Numeric(18,0))
    HOUSE_TYPE_ID = Column(Numeric(18,0))
    MOBILE_1 = Column(String(20))
    MOBILE_2 = Column(String(20))
    EMAIL = Column(String(60))
    CITY_ID = Column(Numeric(18,0))
    REGION_ID = Column(Numeric(18,0))
    CUR_TEL = Column(String(30))
    REG_CITY_ID = Column(Numeric(18,0))
    REG_REGION_ID = Column(Numeric(18,0))
    REG_TEL = Column(String(20))
    RMK = Column(String(4000))    
    COMP_NME = Column(String(100))
    COMP_CITY_ID = Column(Numeric(18,0))
    COMP_REGION_ID = Column(Numeric(18,0))
    COMP_TEL = Column(String(30))  
    COMP_EXT = Column(String(10))  
    COMP_DEPT = Column(String(50))  
    JOB_TITLE = Column(String(50))
    SENIORITY = Column(Numeric(18,0))  
    SALARY = Column(Numeric(18,0))  
    PRD_NUM = Column(Numeric(18,0))  
    IS_NEW_CAR = Column(Numeric(18,0))
    ENG_NO = Column(String(30))
    ISSUE_DT = Column(String(8))
    LINC_NO = Column(String(20))
    MODEL = Column(String(50))
    RENEW_DT = Column(String(8))
    BRAND = Column(String(50))
    CC = Column(Numeric(18,3))
    PROD_YM = Column(String(6))
    CAR_YEARS = Column(Numeric(18,0))
    CRD_USR_ID = Column(String(20))
    CRD_USR_NME = Column(String(50))
    APPEAL_DT = Column(String(8))
    CUST_KIND_CD = Column(String(1))
    JOB_TITLE_ID = Column(Numeric(18,0))
    PROJ_REQ_TYPE_CD = Column(String(4))
    VIOLATE_REG_FLAG = Column(Numeric(18,0))
    PROD_CATG_CD = Column(String(4))
    CRD_WORKING_TIME = Column(Numeric(18,0))
    SECIAL_CASE_CD = Column(String(1))
    GUAR_BUY_BACK_ID = Column(Numeric(18,0))
    NEG_ITEM_IND = Column(Numeric(18,0))
    NEG_ITEM_ID = Column(String(50))
    APP_CRD_STATUS_CD = Column(String(1))
    APPEAL_REASON_TYPE_ID = Column(Numeric(18,0))
    APPEAL_RMK = Column(String(1000))
    CRD_LABER_INS_RESULT_ID = Column(Numeric(18,0))
    STUD_GOV_IND = Column(Numeric(18,0))
    LEHF_FLAG = Column(Numeric(18,0))
    APLY_FORM_TYPE_PROJ_ID = Column(String(30))
    FEE_TYPE_IND = Column(Numeric(18,0))
    ID_CARD_CITY_ID = Column(Numeric(18,0))
    TEL_MKT_IND = Column(Numeric(18,0))
    OTH_ZIP_CD = Column(String(5))
    OTH_CITY_ID = Column(Numeric(18,0))
    OTH_REGION_ID = Column(Numeric(18,0))
    OTH_ADDR = Column(String(200))
    LIMIT_BUY_COMMUN_PRD = Column(Numeric(18,0))
    IS_CO_MARKETING = Column(Numeric(18,0))
    FB_ACCT = Column(String(50))
    LINE_ACCT = Column(String(50))
    IG_ACCT = Column(String(50))
    LAST_COMP_NME = Column(String(100))
    LAST_COMP_DEPT = Column(String(50))
    LAST_JOB_TITLE = Column(String(50))
    PAY_TYPE_CD = Column(String(3))
    PAY_DAY = Column(Numeric(18,0))
    PAYEE_BNK_ID = Column(String(10))
    ORG_ONWR = Column(String(60))
    INSR_COMP = Column(String(60))
    EST_AMT = Column(Numeric(18,0))
    USE_YEAR = Column(Numeric(18,0))
    IS_PHONE_CASE = Column(Numeric(18,0))
    QUOTE_NME = Column(String(160))
    QUOTE_TYPE_NME = Column(String(200))
    SAL_DEPT_NME = Column(String(256))
    SAL_USR_NME = Column(String(50))
    APP_SAL_DEPT_NME = Column(String(256))
    APP_SAL_USR_NME = Column(String(50))
    APPEAL_USR_NME = Column(String(50))
    APPEAL_CRD_USR_NME = Column(String(50))
    GUAR_NME = Column(String(100))
    DATA_PREDICTION_RESULT_P = Column(String(10))
    DATA_PREDICTION_RESULT = Column(String(10))
    FACTORYSERVICE_USR_DEPT_NME = Column(String(256))
    FACTORYSERVICE_USR_NME = Column(String(50))
    MID_RETURN_CODE = Column(String(50))
    MID_RETURN_MSG = Column(String(500))
    PHONE_SALE_SRC_NME = Column(String(200))
    PHONE_SALE_SRC = Column(String(200))
    PHONE_PROD_CATG_NME = Column(String(200))
    CHANNEL_NME = Column(String(200))
    NEW_PROD_CATG_CD = Column(String(4),index=True)
    DATA_SRC = Column(String(1),index=True)
    ELDER_POINTS = Column(Boolean)
    AMOUNT_OVER_100K = Column(Boolean)
    OVER80_CREDIT = Column(Boolean)
    PRD_B04_B10_PTS = Column(Boolean)
    AM_PTS = Column(Boolean)

class AP_MDL_AD_FINAD(Base):
    __tablename__ = 'AP_MDL_AD_FINAD'  # 定义表名
    EDI_NO = Column(String(12),index=True)
    DATA_DATE = Column(String(8),index=True)
    MAJ_SEQ_ID = Column(Numeric(18,0), primary_key=True,index=True)
    APLY_TYPE_ID = Column(Numeric(18,0))
    APP_CASE_ID = Column(String(20))
    EP_CASE_ID = Column(String(20))
    EC_ORDER_ID = Column(String(50))
    MOTO_CASE_MAJ = Column(Numeric(18,0))
    QUICK_RESULT_CD = Column(String(30))
    OLD_APP_NO = Column(String(20))
    APP_NO = Column(String(20))
    INST_CD = Column(String(20))
    COMP_ID = Column(Numeric(18,0))
    CUST_ID = Column(String(10))
    CUST_NME = Column(String(100))
    ID_TYPE_ID = Column(Numeric(18,0))
    SEX = Column(Numeric(18,0))
    BUSN_TYPE_ID = Column(Numeric(18,0))
    VENDER_NO = Column(String(10))
    VENDER_NME = Column(String(120))
    VENDER_CLASS = Column(String(2))
    VENDER_ID2 = Column(String(40))
    VENDER_NME2 = Column(String(120))
    VENDER_CLASS2 = Column(String(2))
    VENDER_ID3 = Column(String(40))
    VENDER_NME3 = Column(String(50))
    VENDER_CLASS3 = Column(String(50))
    VNO2 = Column(String(40))
    IS_RAPID_SERVICE = Column(Numeric(18,0))
    CRD_REPLY_TIME = Column(Numeric(18,0))
    CRD_LIMIT = Column(Numeric(18,0))
    STATUS = Column(String(1))
    START_DT = Column(String(8))
    APLY_DT = Column(String(17))
    NOTICE_TIME = Column(String(17))
    NOTICE_DESC = Column(String(100))
    SECRET_FLAG = Column(Numeric(18,0))
    OBJ_TTL_AMT = Column(Numeric(18,0))
    OBJ_NME = Column(String(300))
    NOTICE_ITEM = Column(String(100))
    MOD_APP_RMK = Column(String(1000))
    BIRTHDAY = Column(String(8))
    MARRIAGE = Column(Numeric(18,0))
    DISABLE_CERT_IND = Column(Numeric(18,0))
    DISABLE_CERT_RMK = Column(String(8))
    ID_CARD_DATE = Column(String(8))
    ID_CARD_TYPE_ID = Column(Numeric(18,0))
    EDU_ID = Column(Numeric(18,0))
    HOUSE_TYPE_ID = Column(Numeric(18,0))
    MOBILE_1 = Column(String(20))
    MOBILE_2 = Column(String(20))
    EMAIL = Column(String(60))
    CITY_ID = Column(Numeric(18,0))
    REGION_ID = Column(Numeric(18,0))
    CUR_TEL = Column(String(30))
    REG_CITY_ID = Column(Numeric(18,0))
    REG_REGION_ID = Column(Numeric(18,0))
    REG_TEL = Column(String(20))
    RMK = Column(String(4000))    
    COMP_NME = Column(String(100))
    COMP_CITY_ID = Column(Numeric(18,0))
    COMP_REGION_ID = Column(Numeric(18,0))
    COMP_TEL = Column(String(30))  
    COMP_EXT = Column(String(10))  
    COMP_DEPT = Column(String(50))  
    JOB_TITLE = Column(String(50))
    SENIORITY = Column(Numeric(18,0))  
    SALARY = Column(Numeric(18,0))  
    PRD_NUM = Column(Numeric(18,0))  
    IS_NEW_CAR = Column(Numeric(18,0))
    ENG_NO = Column(String(30))
    ISSUE_DT = Column(String(8))
    LINC_NO = Column(String(20))
    MODEL = Column(String(50))
    RENEW_DT = Column(String(8))
    BRAND = Column(String(50))
    CC = Column(Numeric(18,3))
    PROD_YM = Column(String(6))
    CAR_YEARS = Column(Numeric(18,0))
    CRD_USR_ID = Column(String(20))
    CRD_USR_NME = Column(String(50))
    APPEAL_DT = Column(String(8))
    CUST_KIND_CD = Column(String(1))
    JOB_TITLE_ID = Column(Numeric(18,0))
    PROJ_REQ_TYPE_CD = Column(String(4))
    VIOLATE_REG_FLAG = Column(Numeric(18,0))
    PROD_CATG_CD = Column(String(4))
    CRD_WORKING_TIME = Column(Numeric(18,0))
    SECIAL_CASE_CD = Column(String(1))
    GUAR_BUY_BACK_ID = Column(Numeric(18,0))
    NEG_ITEM_IND = Column(Numeric(18,0))
    NEG_ITEM_ID = Column(String(50))
    APP_CRD_STATUS_CD = Column(String(1))
    APPEAL_REASON_TYPE_ID = Column(Numeric(18,0))
    APPEAL_RMK = Column(String(1000))
    CRD_LABER_INS_RESULT_ID = Column(Numeric(18,0))
    STUD_GOV_IND = Column(Numeric(18,0))
    LEHF_FLAG = Column(Numeric(18,0))
    APLY_FORM_TYPE_PROJ_ID = Column(String(30))
    FEE_TYPE_IND = Column(Numeric(18,0))
    ID_CARD_CITY_ID = Column(Numeric(18,0))
    TEL_MKT_IND = Column(Numeric(18,0))
    OTH_ZIP_CD = Column(String(5))
    OTH_CITY_ID = Column(Numeric(18,0))
    OTH_REGION_ID = Column(Numeric(18,0))
    OTH_ADDR = Column(String(200))
    LIMIT_BUY_COMMUN_PRD = Column(Numeric(18,0))
    IS_CO_MARKETING = Column(Numeric(18,0))
    FB_ACCT = Column(String(50))
    LINE_ACCT = Column(String(50))
    IG_ACCT = Column(String(50))
    LAST_COMP_NME = Column(String(100))
    LAST_COMP_DEPT = Column(String(50))
    LAST_JOB_TITLE = Column(String(50))
    PAY_TYPE_CD = Column(String(3))
    PAY_DAY = Column(Numeric(18,0))
    PAYEE_BNK_ID = Column(String(10))
    ORG_ONWR = Column(String(60))
    INSR_COMP = Column(String(60))
    EST_AMT = Column(Numeric(18,0))
    USE_YEAR = Column(Numeric(18,0))
    IS_PHONE_CASE = Column(Numeric(18,0))
    QUOTE_NME = Column(String(160))
    QUOTE_TYPE_NME = Column(String(200))
    SAL_DEPT_NME = Column(String(256))
    SAL_USR_NME = Column(String(50))
    APP_SAL_DEPT_NME = Column(String(256))
    APP_SAL_USR_NME = Column(String(50))
    APPEAL_USR_NME = Column(String(50))
    APPEAL_CRD_USR_NME = Column(String(50))
    GUAR_NME = Column(String(100))
    DATA_PREDICTION_RESULT_P = Column(String(10))
    DATA_PREDICTION_RESULT = Column(String(10))
    FACTORYSERVICE_USR_DEPT_NME = Column(String(256))
    FACTORYSERVICE_USR_NME = Column(String(50))
    MID_RETURN_CODE = Column(String(50))
    MID_RETURN_MSG = Column(String(500))
    PHONE_SALE_SRC_NME = Column(String(200))
    PHONE_SALE_SRC = Column(String(200))
    PHONE_PROD_CATG_NME = Column(String(200))
    CHANNEL_NME = Column(String(200))
    NEW_PROD_CATG_CD = Column(String(4),index=True)
    DATA_SRC = Column(String(1),index=True)
    ELDER_POINTS = Column(Boolean)
    AMOUNT_OVER_100K = Column(Boolean)
    OVER80_CREDIT = Column(Boolean)
    PRD_B04_B10_PTS = Column(Boolean)
    AM_PTS = Column(Boolean)
    AD_SCORE = Column(Numeric(18,6))