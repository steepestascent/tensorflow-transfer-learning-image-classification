
import tensorflow as tf
import os

image_reader = tf.WholeFileReader()
dir_path = os.path.dirname(os.path.realpath(__file__))

extension = ['jpg', 'jpeg', 'png', 'gif']
for ext in extension:
    file_names = []
    for subdir, dirs, files in os.walk(os.path.join(dir_path, 'dogs')):
        for f in files:
            if f.lower().endswith(ext):
                file_names.append(os.path.join(subdir, f))
    
    _, image_file = image_reader.read(tf.train.string_input_producer(file_names)) # Start a new session to show example output.
    image = tf.image.decode_png(image_file)
    
    with tf.Session() as sess:
        # Required to get the filename matching to run.
        tf.initialize_all_variables().run()
    
        # Coordinate the loading of image files.
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord)
    
        # Get an image tensor and print its value.
        samples = 0
        for i in range(len(file_names)):
            try:
                image_tensor, full_path = sess.run([image, _])
                print(full_path.decode())
                os.rename(full_path.decode(),  os.path.join(os.path.dirname(full_path.decode()), "data-sample-{}.{}".format(samples, ext)))
                samples = samples + 1
            except Exception as ex:
                print('Error decoding image. Moving to next image.')
    
        print("Number of samples for {}: {}".format(samples, ext))
    
        # Finish off the filename queue coordinator.
        coord.request_stop()
        coord.join(threads)