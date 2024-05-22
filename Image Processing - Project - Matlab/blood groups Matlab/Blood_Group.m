function Blood_Group(Image)
%--------------------------------------------------------------(Report Second-step)
%---->Display the original image and a grayscale copy of it:- 
figure;
subplot(1,2,1);
imshow(Image);  
title('Original Image');

Image2 = rgb2gray(Image);
subplot(1,2,2);
imshow(Image2);
title('Grayscale image');
%--------------------------------------------------------------
%----> Crop the image into sub-images each of them containing 
% one of the blood slice Anti's:-
figure;

Anti_A = Image2(6:175, 30:170);
subplot(2,2,1);
imshow(Anti_A);
title('ANTI-A');

Anti_B = Image2(6:175, 210:350);
subplot(2,2,2);
imshow(Anti_B);
title('ANTI-B');

Anti_D = Image2(6:175, 360:530);
subplot(2,2,3);
imshow(Anti_D);
title('ANTI-D');

%--------------------------------------------------------------
%---->To see the histogram for this image:-
% figure;
% imhist(Anti_A); 
%--------------------------------------------------------------

%(Report Third-step)

Bcount = 0;  %To store the frequency for the black intensities  
[x y] = size(Anti_A);
for i = 1:x
   for j = 1:y 
       if(Anti_A(i,j) >= 60 && Anti_A(i,j) <= 120)
           Bcount = Bcount + 1;
       end
   end
end

%________________________________
%->Check the black pixles count:-
% display('Bcount A'); 
% Bcount
%________________________________

% After every calculation for ANTI's we need to compare 
% the black pixels count with the max pixel range for
% black to know if it is colored or not:- 
if Bcount >= 8000
    A = 1;
else
    A = 0;
end
%--------------------------------------------------------------
Bcount = 0;
[x y] = size(Anti_B);
for i = 1:x
   for j = 1:y 
       if(Anti_B(i,j) >= 60 && Anti_B(i,j) <= 120)
           Bcount = Bcount + 1;
       end
   end
end

%________________________________
%->Check the black pixles count:-
% display('Bcount B'); 
% Bcount
%________________________________

if Bcount >= 8000
    B = 1;
else
    B = 0;
end
%--------------------------------------------------------------
Bcount = 0;
[x y] = size(Anti_D);
for i = 1:x
   for j = 1:y 
       if(Anti_D(i,j) >= 60 && Anti_D(i,j) <= 120)
           Bcount = Bcount + 1;
       end
   end
end

%________________________________
%->Check the black pixles count:-
% display('Bcount D'); 
% Bcount
%________________________________

if Bcount >= 8000
    C = 1; 
else
    C = 0;
end

%--------------------------------------------------------------
%(Report Fourth & Fifth-step)

if(A == 0 && B == 1 && C == 0)
    display('Blood type for this slice is ( A+ )'); 
    
elseif(A == 0 && B == 1 && C == 1)
    display('Blood type for this slice is ( A- )'); 
    
elseif(A == 1 && B == 0 && C == 0)
    display('Blood type for this slice is ( B+ )'); 

elseif(A == 1 && B == 0 && C == 1)
    display('Blood type for this slice is ( B- )'); 

elseif(A == 0 && B == 0 && C == 0)
    display('Blood type for this slice is ( AB+ )'); 
    
elseif(A == 0 && B == 0 && C == 1)
    display('Blood type for this slice is ( AB- )'); 
    
elseif(A == 1 && B == 1 && C == 0)
    display('Blood type for this slice is ( O+ )'); 

else
    display('Blood type for this slice is ( O- )'); 
end

end
