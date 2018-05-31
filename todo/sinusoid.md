Categories: core
Tags: sinusoid

## Sinusoid ##

- Function of time.
- Generalised sinusoid defined by:

      $latex f(t)=Acos(\omega t+\phi) $

- where:
  - $latex A $ - amplitude (maximum value of sinusoid).
  - $latex \omega $ - radian frequency (angular frequency).
  - $latex \phi $ - phase angle (radians)

### Frequency ###

    $latex frequency=f=\frac{{\displaystyle 1}}{{\displaystyle T}}Hz $

    $latex w=2\pi f \; radian/s $
    
    $latex \omega=2\pi{\displaystyle \frac{\Delta t}{T}}radians=360\frac{{\displaystyle \Delta t}}{{\displaystyle T}}degrees $

### Average ###

      $latex \left\langle x(t)\right\rangle ={\displaystyle \frac{1}{T}}{\displaystyle \intop_{0}^{T}x(t^{,})dt^{,}} $

- e.g.

      $latex x(t)=10cos(100t) $

      $latex \therefore T={\displaystyle \frac{2\pi}{\omega}}=\frac{{\displaystyle 2\pi}}{{\displaystyle 100}} $

      $latex \left\langle x(t)\right\rangle ={\displaystyle \frac{1}{T}}{\displaystyle \intop_{0}^{2\pi/100}10cos(100t)dt} $

      $latex \left\langle x(t)\right\rangle =\frac{{\displaystyle 10}}{{\displaystyle 2\pi}}\left\langle sin(2\pi)-sin(0)\right\rangle =0 $

- i.e. average value is 0 independent of amplitude and frequency.
- Note,

      $latex \left\langle A\, cos(\omega t+\phi)\right\rangle =0 $

- Therefore, consider using Root Mean Square (RMS), i.e.

      $latex x\_{RMS}=\sqrt{\frac{{\displaystyle 1}}{{\displaystyle T}}{\displaystyle \intop\_{0}^{T}}x^{2}(t^{,})dt^{,}} $


### Notes ###

- $latex A $ occurs at $latex cos(\omega t+\phi)=1 $.
- $latex \omega $ defines how often the maxima occurs:
  - i.e. when $latex cos \theta = 0 $ i.e. at $latex t=t_{0} $

        $latex (\omega t_{0}+\phi)=0\qquad(i) $

  - when sinusoid at maximum, will reach maximum in $latex 2\pi $

        $latex (\omega t_{0}+\phi)=2\pi\qquad(ii) $

  - therefore:

        $latex (i)-(ii)=\omega (t\_{1}-t\_{0}) = 2\pi $

- The time elapsed between maxima ($latex T $) is defined as:

        $latex T\equiv t_{1}-t_{0} $

        $latex \therefore T=\frac{{\displaystyle 2\pi}}{{\displaystyle \omega}} $

- The choice of sine/consine irrelevant, since any cos angle can be represented by any sine angle with a phase shift of $latex \frac{{\displaystyle \pi}}{{\displaystyle 2}} $.
- i.e.

        $latex A\, sin(\omega t)=A\, cos(\omega t-\frac{{\displaystyle \pi}}{2}) $

- Note, for a periodic signal:

        $latex x(t)=x(t+nT) $ for $latex n=1,2... $
  
  - where $latex T $ is the period of $latex x(t) $.



