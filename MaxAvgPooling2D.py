import tensorflow as tf

def MaxAvgPooling2D(m,n, model): 
    max = tf.keras.layers.MaxPool2D(pool_size=(2,2), strides=1, padding='SAME')(model)
    avg = tf.keras.layers.AveragePooling2D(pool_size=(2,2), strides=1, padding='SAME')(model)
    
    model = (max*m + avg*n)/(m+n)

    return model
