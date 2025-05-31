import tensorflow as tf
import os


def setup_tensorflow_environment():
    # Physical devices configuration
    physical_devices = tf.config.list_physical_devices()
    print("Available devices:", physical_devices)

    # Configure GPU
    try:
        if tf.config.list_physical_devices('GPU') == 1 :
            tf.config.experimental.set_memory_growth(physical_devices[1], True)

        # Set compute units (GPU cores) utilization
        tf.config.experimental.set_virtual_device_configuration(
            physical_devices[1],
            [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=24576)]  # 24GB RAM allocation
        )
    except:
        print("No GPU devices found")

    # CPU configuration
    tf.config.threading.set_intra_op_parallelism_threads(7)  # Match your CPU cores
    tf.config.threading.set_inter_op_parallelism_threads(7)  # Match your CPU cores

    # Mixed precision configuration
    tf.keras.mixed_precision.set_global_policy('mixed_float16')

    # XLA optimization
    tf.config.optimizer.set_jit(False)

    # Additional performance configurations
    os.environ['TF_GPU_THREAD_MODE'] = 'gpu_private'
    os.environ['TF_GPU_THREAD_COUNT'] = '30'  # Match your GPU cores
    os.environ['TF_USE_CUDNN_BATCHNORM_SPATIAL_PERSISTENT'] = '1'
    os.environ['TF_ENABLE_AUTO_MIXED_PRECISION'] = '1'
    
    # Metal performance configuration
    os.environ['METAL_DEBUG_ERROR_MODE'] = '0'
    os.environ['METAL_DEVICE_WRAPPER_TYPE'] = '0'
