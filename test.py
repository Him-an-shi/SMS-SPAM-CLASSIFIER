<<<<<<< HEAD
import pickle
from sklearn.utils.validation import check_is_fitted

model = pickle.load(open('model.pkl', 'rb'))

print(type(model))

try:
    check_is_fitted(model)
    print("MODEL IS FITTED")
except Exception as e:
    print("MODEL IS NOT FITTED")
=======
import pickle
from sklearn.utils.validation import check_is_fitted

model = pickle.load(open('model.pkl', 'rb'))

print(type(model))

try:
    check_is_fitted(model)
    print("MODEL IS FITTED")
except Exception as e:
    print("MODEL IS NOT FITTED")
>>>>>>> 7049b5fa395747c038a5d8908fe7f3ea18deb128
    print(e)