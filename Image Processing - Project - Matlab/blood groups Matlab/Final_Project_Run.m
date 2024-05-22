clc
clear all
%------------------------------
%Read an image to be processed - (Report First-step)
[n, d] = uigetfile();
f = fullfile(d,n); 
image = imread(f);  % choose an image to be proccessed
b = dec2bin(image,8) - '0'; 
Blood_Group(image);