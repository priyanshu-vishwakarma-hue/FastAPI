from database import engine, Base
import model    # this loads the model.py file so that metadata is EMPTY. Because Book class was never loaded if not import model.


Base.metadata.create_all(bind=engine)