import torch

# Root directory for dataset
dataset_name = "celeba"
data_root = f"datasets/{dataset_name}/"
# data_root = f"datasets/{dataset_name}/"
model_root = "models/DCGAN/"
results_root = "results/DCGAN/"

# seed
manualSeed = 999

# Number of workers for dataloader
workers = 2

# Batch size during training
batch_size = 128

# Spatial size of training images. All images will be resized to this
#   size using a transformer.
image_size = 64

# Number of channels in the training images. For color images this is 3
nc = 3

# Size of z latent vector (i.e. size of generator input)
nz = 100

# Size of feature maps in generator
ngf = 64

# Size of feature maps in discriminator
ndf = 64

# Number of training epochs
num_epochs = 50

# Learning rate for optimizers
lr = 0.0002

# Beta1 hyperparameter for Adam optimizers
beta1 = 0.5

# Number of GPUs available. Use 0 for CPU mode.
ngpu = 4

# Establish convention for real and fake labels during training
real_label = 1.0
fake_label = 0.0

# Create batch of latent vectors that we will use to visualize
#  the progression of the generator
fixed_noise = torch.randn(64, nz, 1, 1, device="cuda")
