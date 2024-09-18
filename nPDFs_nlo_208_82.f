
!
! Nuclear parton distribution functions with uncertainties in the general mass variable flavor number scheme
! Hamzeh Khanpour, Maryam Soleymaninia, S. Atashbar Tehrani, Hubert Spiesberger, Vadim Guzey
!                               e-Print: arXiv:2010.00555 [hep-ph];	Phys. Rev. D 104 (2021) 034010
!


! An example Code for KSASG20 nuclear PDFs
!  
! --    Compile with:
! --    gfortran nPDFs_nlo_208_82.f -L /home/hamzeh-khanpour/local/lib -lLHAPDF -o nPDFs_nlo_208_82
! --    ./nPDFs_nlo_208_82
! ---------------------------------------


       program KSASG20

       implicit none
       integer nset, nmem, imem, MaxNumSets, nx, i, ix
       double precision x(1000), q2, q, xf(-6:6), xs(0:100),
     +       xf0, xfp, xfm, xfs, correlation, xminimum, xmaximum
       logical lMonteCarlo, lSymmetric
       
       character*10 lhaversion
       
       data Q2/100.0D0/,  nset/1.D0/

  !-- Get the LHAPDF version number.
       call getlhapdfversion(lhaversion)
       write(6,*) "LHAPDF Version = ", lhaversion

  !-- Get the maximum number of concurrent PDF sets.
       call GetMaxNumSets(MaxNumSets)
       write(6,*) "MaxNumSets = ", MaxNumSets
       write(6,*)
       

  !-- Test three PDF sets that have different uncertainty calculations.      
   
        call InitPDFSetByNameM(nset,"nPDFs_nlo_208_82")  !!! For the central value
    
       call numberPDFM(nset,nmem)
       
       write(6,*) "PDF set = ", nset
        write(6,*) "Number of PDF members = ", nmem

c     !-- Check if Monte Carlo PDF set (NNPDF) or if
c     !-- should compute symmetric errors (Alekhin).

       call GetPDFUncTypeM(nset,lMonteCarlo,lSymmetric)
       write(6,*) "lMonteCarlo = ", lMonteCarlo
       write(6,*) "lSymmetric = ", lSymmetric
       write(6,*)
       

       nx = 1000
       xminimum = 0.001D0
       xmaximum = 0.999D0
       DO ix = 1, nx
         x(ix) = 10.D0**(log10(xminimum) + (ix-1.D0)/(nx-1.D0)*
     -        (log10(xmaximum) - log10(xminimum)))
       end Do

       Q = SQRT(Q2)
       
       do i = 1, nx
       xf0 = 0.D0 ! central value
       xfp = 0.D0 ! positive uncertainty
       xfm = 0.D0 ! negative uncertainty
       xfs = 0.D0 ! symmetrised uncertainty


       do imem = 0, nmem
        call InitPDFM(nset,imem)
        call evolvePDFM(nset,x(i),q,xf)

         xs(imem) = xf(0)
        
       end do
       
       open (10, file='xg-Q2-100GeV2.dat')
       

       call GetPDFuncertaintyM(nset,xs,xf0,xfp,xfm,xfs)
      
       write(10,*) x(i),  xf0
 
       write(*,*)  x(i),  xf0
      

       end do

       stop
       end program KSASG20
