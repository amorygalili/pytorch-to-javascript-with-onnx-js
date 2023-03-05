import torch

from inference_mnist_model import Net


def main():

    # Set the path of the .torchscript file
  path = "charged_up_2023-02-27.torchscript"

  # Load the .torchscript file
  model = torch.jit.load(path)


  # pytorch_model = Net()
  # pytorch_model.load_state_dict(torch.load('charged_up_2023-02-27.torchscript'))
  # pytorch_model.eval()
  # dummy_input = torch.zeros(280 * 280 * 4)
  # torch.onnx.export(pytorch_model, dummy_input, 'onnx_model.onnx', verbose=True)


if __name__ == '__main__':
  main()
