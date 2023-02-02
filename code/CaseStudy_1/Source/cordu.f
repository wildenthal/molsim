**==coru.spg  processed by SPAG 4.52O  at 18:54 on 27 Mar 1996
      FUNCTION CORDU(R, Rho, Lambda)
c
c     tail correction for the d_energy:
c
c  CORDU(output) d_energy tail correction
c  R    (input)  cutoff radius
c  Rho  (input)  density
c
 
      IMPLICIT NONE
      INCLUDE 'potential.inc'
      DOUBLE PRECISION sig3, ri3, R, CORDU, Rho, Lambda
 
      sig3 = SIG2*SQRT(SIG2)
      ri3 = sig3/(R*R*R)
      CORDU = 2*PI*EPS4*(Rho*sig3)*(ri3*ri3*ri3*5*Lambda**4/9-
     &ri3*Lambda**2)
      RETURN
      END
