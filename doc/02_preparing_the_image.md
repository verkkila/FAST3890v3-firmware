OOB format is 9 bytes FF, 7 bytes ECC
Image below is the OOB section of the first page in the dump
![[Pasted image 20251101021115.png]]
Stored ECC can be computed using this tool
https://github.com/StrayLightning/brcm-nand-bch
BCH params are:
m = 14
t = 4
prim_poly = 0x5803 = 22531

In the image below the calculated ECC for each sector is printed out.
![[Pasted image 20251101021334.png]]
The stored ECC (above) matches the calculated ECC (below) which confirms the validity of the BCH params. We can now run decode for the dumped image:
![[Pasted image 20251101021957.png]]

