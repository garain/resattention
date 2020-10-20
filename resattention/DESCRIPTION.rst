# resattention
---------------

A python library for implementing a Residual Attention Convolutional Neural Network
and training it for image classification problems. This model supports multi-class
classification and is easy to use both for training and testing purposes.

The code is Python 2 and 3 compatible.

# Installation
--------------

Fast install:
-------------

::

        pip install resattention

For a manual install get this package:
--------------------------------------

.. code:: bash

        $wget https://github.com/garain/resattention/archive/master.zip
        $unzip master.zip
        $rm master.zip
        $cd resattention-master

Install the package:
--------------------

::

        python setup.py install    

# Example
---------

.. code:: python

        from resattention import models
        import tensorflow as tf

        model = models.AttentionResNetCifar10(shape=(32,32,3),n_classes=2,n_channels=3)#RGB images
        model = models.AttentionResNetCifar10(shape=(32,32,1),n_classes=6,n_channels=1)#GrayScale images
        
        model.compile(tf.keras.optimizers.Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
        model.summary()


# Models supported
------------------
 - AttentionResNetCifar10
 - AttentionResNet92
 - AttentionResNet56