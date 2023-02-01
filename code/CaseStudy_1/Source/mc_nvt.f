**==mc_nvt.spg  processed by SPAG 4.52O  at 18:54 on 27 Mar 1996
      PROGRAM MC_NVT
c________________________________________________________________________
c
c   Understanding Molecular Simulations: From Algorithms to Applications
c
c                 Daan Frenkel  and  Berend Smit
c
c  We make no warranties, express or implied, that the programs contained
c  in this work are free of error, or that they will meet your requirements
c  for any particular application. They should not be relied on for solving
c  problems whose incorrect solution could results in injury, damage, or
c  loss of property. The authors and publishers disclaim all liability for
c  direct or consequential damages resulting from your use of the programs
c
c__________________________________________________________________________
c
c
c   Case Study 1: Equation of state of the Lennard-Jones fluid
c
c__________________________________________________________________________
 
      IMPLICIT NONE
      INTEGER iseed, equil, prod, nsamp, ii, icycl, ndispl, attempt, 
     &        nacc, ncycl, nmoves, imove
      DOUBLE PRECISION en, ent, vir, virt, dr, den, dent
      DOUBLE PRECISION dens, denc, dena, denb, lambda
      DOUBLE PRECISION den2s, den2c, den2a, den2b
c     ---initialize values for dE/dL accumulator
      dens = 0.D0
      denc = 0.D0
      WRITE (6, *) '**************** MC_NVT ***************'
c     ---initialize sysem
      CALL READDAT(equil, prod, nsamp, ndispl, dr, iseed, lambda)
      nmoves = ndispl
c     ---total energy of the system
      CALL TOTERG(en, vir, den, lambda)
      WRITE (6, 99001) en, vir, den
c     ---start MC-cycle
      DO ii = 1, 2
c        --- ii=1 equilibration
c        --- ii=2 production
         IF (ii.EQ.1) THEN
            ncycl = equil
            IF (ncycl.NE.0) WRITE (6, *) ' Start equilibration '
         ELSE
            IF (ncycl.NE.0) WRITE (6, *) ' Start production '
            ncycl = prod
         END IF
         attempt = 0
         nacc = 0
c        ---intialize the subroutine that adjust the maximum displacement
         CALL ADJUST(attempt, nacc, dr)
         DO icycl = 1, ncycl
            DO imove = 1, nmoves
c              ---attempt to displace a particle
               CALL MCMOVE(en, vir, attempt, nacc, dr, iseed, den, 
     &                                                           lambda)
            END DO
            IF (ii.EQ.2) THEN
c              ---sample averages
               IF (MOD(icycl,nsamp).EQ.0) CALL SAMPLE(icycl, en, vir, 
     &                                                              den)
c              ---sum den values with Kahan algorithm
               dena = den - denc
               denb = dens + dena
               denc = (denb - dens) - dena
               dens = denb
               
c              ---sum square of values with Kahan
               den2a = den**2 - den2c
               den2b = den2s + den2a
               den2c = (den2b - den2s) - den2a
               den2s = den2b

            END IF
            IF (MOD(icycl,ncycl/5).EQ.0) THEN
               WRITE (6, *) '======>> Done ', icycl, ' out of ', ncycl
c              ---write intermediate configuration to file
               CALL STORE(8, dr)
c              ---adjust maximum displacements
               CALL ADJUST(attempt, nacc, dr)
            END IF
         END DO
         dens = dens/prod
         den2s = den2s/prod - dens**2
         IF (ii.EQ.2) THEN
            WRITE (666, *) lambda, dens, den2s
         END IF
         IF (ncycl.NE.0) THEN
            IF (attempt.NE.0) WRITE (6, 99003) attempt, nacc, 
     &                               100.*FLOAT(nacc)/FLOAT(attempt)
c           ---test total energy
            CALL TOTERG(ent, virt, dent, lambda)
            IF (ABS(ent-en).GT.1.D-6) THEN
               WRITE (6, *) 
     &                    ' ######### PROBLEMS ENERGY ################ '
            END IF
            IF (ABS(virt-vir).GT.1.D-6) THEN
               WRITE (6, *) 
     &                    ' ######### PROBLEMS VIRIAL ################ '
            END IF
            WRITE (6, 99002) ent, en, ent-en, virt, vir, virt-vir,
     &                       dent, den, dent-den, dens
         END IF
      END DO
      CALL STORE(21, dr)
      STOP
 
99001 FORMAT (' Total energy initial configuration: ', f12.5, /, 
     &        ' Total virial initial configuration: ', f12.5 /,
     &        ' Value  dE/dL initial configuration: ', f12.5)
99002 FORMAT (' Total energy end of simulation    : ', f12.5, /, 
     &        '       running energy              : ', f12.5, /, 
     &        '       difference                  : ', e12.5, /, 
     &        ' Total virial end of simulation    : ', f12.5, /, 
     &        '       running virial              : ', f12.5, /, 
     &        '       difference                  : ', e12.5 /,
     &        ' Value dE/dL at end of simulation  : ', f12.5 /,
     &        '       running dE/dL               : ', f12.5 /,
     &        '       difference                  : ', f12.5 /,
     &        ' Ensemble average dE/dL            : ', f12.5)
99003 FORMAT (' Number of att. to displ. a part.  : ', i10, /, 
     &        ' success: ', i10, '(= ', f5.2, '%)')
      END
