OOB format is 9 bytes FF, 7 bytes ECC  
Image below is the OOB section of the first page in the dump  
![](img_oob.png)  
Stored ECC can be computed using this tool  
https://github.com/StrayLightning/brcm-nand-bch  
BCH params are:  
m = 14  
t = 4  
prim_poly = 0x5803 = 22531  

In the image below the calculated ECC for each sector is printed out.  
![](img_calculated_ecc.png)  
The stored ECC (above) matches the calculated ECC (below) which confirms the validity of the BCH params. We can now run decode for the dumped image:  
![](img_decode_results.png)  

