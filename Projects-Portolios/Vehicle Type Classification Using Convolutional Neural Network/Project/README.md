# Vehicle-Type-Classification-Using-CNN
<p>This project is about vehicle type classification using convolutional neural network. And we build three CNN models to solve this problem.</p>
<p>This repository cotains a scientific blog <a href=“./Blog-Vehicle Type Classification using CNN.ipynb">Vehicle Type Classification using CNN </a>about how to implement this project including how to set up the deep learning environment, code details, the results of three CNN models and our evaluation and conclusion.</p>
<p>You can access and download the dataset we use in <a href="http://iitlab.bit.edu.cn/mcislab/vehicledb/" target="_blank">BIT-Vehicle Dataset</a></p>
<p>We suggest you using GPU to train these CNN models because of the computational efficiency.</p>
<p>Here are some instructions about how to set up an AWS Environment:</p>
<b>Instruction:</b><br>
(1) Create an AWS account https://aws.amazon.com/ and sign in to the console.<br>
(2) Then you can see your dashboard and make sure that you selected Frankfurt, N. Virgiania, or Singapore as your region.<br>
(3) From AWS Service choose EC2 (“Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity in the Amazon Web Services (AWS) cloud. Using Amazon EC2 eliminates your need to invest in hardware up front, so you can develop and deploy applications faster).<br>
(4) Click "Launch Instance" blue button to launch your instance.<br>
(5) Choose Deep Learning AMI(Ubuntu) with pre-installed Keras, TensorFlow etc.<br>
(6) Configure your instance step by step following the instruction.<br>
(7) Configure your "Security Group". This stage is important, because you’ll want to access your instance not only using ssh, but also via browser. Add a custom TCP rule on port 8888. Make it accessible only from your IP address, both 8888 and 22(ssh).<br>
(8) Finally, everything is ready, and you can launch the instance.<br>
(9) Open your terminal and connect to AWS instance using SSH.<br>
(10) Run the Jupyter Notebook with this command:  `Jupyter Notebook`<br>
If you want to see more details for AWS EC2 instance tutorial can refer to this blog: <a href="https://hackernoon.com/keras-with-gpu-on-amazon-ec2-a-step-by-step-instruction-4f90364e49ac" target = "_blank">Keras with GPU on Amazon EC2 – a step-by-step instruction</a>
