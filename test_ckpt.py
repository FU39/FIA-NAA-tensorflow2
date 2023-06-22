import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

ckpt_path = './models_tf/adv_inception_resnet_v2/adv_inception_resnet_v2.ckpt'
saver = tf.train.import_meta_graph(ckpt_path+'.meta', clear_devices=True)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver.restore(sess, ckpt_path)
