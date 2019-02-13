# Writing Style Transfer using Variational Autoencoders fed to Generative Adversarial Networks
> Ayush Singh, Ritu Palod {singh.ay, palod.r\}@husky.neu.edu
----

<!-- ##### This repository contains implementation code. -->

## Introduction
Past decade has seen the exponential increase in computational capacity of computers and getting cheaper at the same time. This has lead to the emergence of big data and hence opened new doors to solve problems hungry for the marriage of very large data sets with machine learning algorithms ushering humanity into an era where computers could not only automate mundane tasks and crunch astronomical numbers, but also achieve superhuman skills in recognizing cat from dogs, and classifying them into thousands of breeds all by learning the hidden structures in features of dog vs cat and helping mathematicians write formulas for high energy experiments to find new quantum particles.

Among all things, deep learning has helped pick up slack in computer vision, speech synthesis and machine translation taking the task of careful feature engineering from domain experts and landing it in the hands of mathematicians and software engineers who could build the infrastructure and functions to automatically learn subtle features by looking at numerous samples. In 1991, it was proved that giving the right parameters a neural network can model any function that can take x as input and output y. Learning the right parameters here has now become one of the primitive areas of research since last few years. This is where the concept of Generative Adversarial Networks (GANs) by Goodfellow gets deep learning a home run by giving us another perspective on unsupervised learning and getting more out of data than just a stochastic gradient descent.

In a nutshell, GANs by \cite{goodfellow2014generative} borrow from game theory the concept of letting two systems compete to outdo the other by training two separate networks with competitive goals to reach an equilibrium of optimal states. One network produces answers (generative) another network distinguishes between the real and the generated answers (adversarial). The concept is to train these networks competitively so that after some time, neither network can make further progress against the other. Or the generator becomes so effective that the adversarial network cannot distinguish between real and synthetic solutions, even with unlimited time and substantial resources. GANs have been extraordinary in generating vivid images given other images,  but cannot be directly applied to natural language as the space in which sentence is present is not continuous and thereby not differentiable. To make it clear, tolerance in noise/variance in images has high interpreted ability but swapping a character with another in a word will most likely result in gibberish which can just be slight as the space of sentences is not continuous. So, when you want to update the generated sentence slightly according to discriminator's behavior, you may not get a sentence.

License
----

MIT