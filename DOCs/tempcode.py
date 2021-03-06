

from __future__ import division

def imagedisp(input):
  return("\includegraphics[width=3in]{"+input+"}")
#Takes input of sympy matrix and outputs pmatrix in LaTeX.
def display_matrix(matrix):
  a=matrix
  i=0
  matsri='\\begin{pmatrix}'
  while i < len(a[0,:]):
    j=0
    while j < len(a[:,0]):
      matsri=matsri+str(a[i,j])
      if j !=len(a[:,0])-1:
        matsri=matsri+'&'
      j=j+1
    if i !=  len(a[0,:])-1:
      matsri=matsri+'\\\\'
    i=i+1
  matsri=matsri+'\end{pmatrix}'
  return(matsri)
    


def output(content):
  file=open("outputfc_5.txt","w")
  file.write(content)
  file.close()


def scrinc(*options):
   if len(options)==0:
      x="""
!bs!definecolor{codegreen}{rgb}{0,0.6,0}
!bs!definecolor{codegray}{rgb}{0.5,0.5,0.5}
!bs!definecolor{codepurple}{rgb}{0.58,0,0.82}
!bs!definecolor{backcolour}{rgb}{0.95,0.95,0.92}

      !bs!lstdefinestyle{mystyle5}{
      backgroundcolor=!bs!color{codegray},   
      commentstyle=!bs!color{magenta},
      keywordstyle=!bs!color{blue},
      linewidth=6in,
      numberstyle=!bs!tiny!bs!color{codegray},
      stringstyle=!bs!color{codepurple},
      basicstyle=!bs!footnotesize,
      breakatwhitespace=false,         
      breaklines=true,                 
      captionpos=b,                    
      keepspaces=true,                 
      numbers=left,                    
      numbersep=5pt,                  
      showspaces=false,                
      showstringspaces=false,
      showtabs=false,                  
      tabsize=2
      }
      %.................................................
!bs!begin{lstlisting}[language=python,style=mystyle5]
def adder(a):
  return(a+1)
output(scrinc('HF'))
!bs!end{lstlisting}
          """
   elif "HF" in options:
      x="""
!bs!definecolor{codegreen}{rgb}{0,0.6,0}
!bs!definecolor{codegray}{rgb}{0.5,0.5,0.5}
!bs!definecolor{codepurple}{rgb}{0.58,0,0.82}
!bs!definecolor{backcolour}{rgb}{0.95,0.95,0.92}

      !bs!lstdefinestyle{mystyle5}{
      backgroundcolor=!bs!color{codegray},   
      commentstyle=!bs!color{magenta},
      keywordstyle=!bs!color{blue},
      linewidth=6in,
      numberstyle=!bs!tiny!bs!color{codegray},
      stringstyle=!bs!color{codepurple},
      basicstyle=!bs!footnotesize,
      breakatwhitespace=false,         
      breaklines=true,                 
      captionpos=b,                    
      keepspaces=true,                 
      numbers=left,                    
      numbersep=5pt,                  
      showspaces=false,                
      showstringspaces=false,
      showtabs=false,                  
      tabsize=2
      }
      %.................................................
!bs!begin{lstlisting}[language=python,style=mystyle5]
<script=python2.7:action={!!sid=1!!!!LinNoId=1!!}>
def adder(a):
  return(a+1)
output(scrinc('HF'))
</script>!bs!end{lstlisting}
          """
   findrep={'!bs!b':'\\b','!bs!n':'\\\\n','!bs!':'\\'}
   for key in findrep:
      x=x.replace(key,findrep[key])
   return(x)


def adder(a):
  return(a+1)
output(scrinc('HF'))


def output(content):
  file=open("outputfc_6.txt","w")
  file.write(content)
  file.close()


def scrinc(*options):
   if len(options)==0:
      x="""
!bs!definecolor{codegreen}{rgb}{0,0.6,0}
!bs!definecolor{codegray}{rgb}{0.5,0.5,0.5}
!bs!definecolor{codepurple}{rgb}{0.58,0,0.82}
!bs!definecolor{backcolour}{rgb}{0.95,0.95,0.92}

      !bs!lstdefinestyle{mystyle6}{
      backgroundcolor=!bs!color{codegray},   
      commentstyle=!bs!color{magenta},
      keywordstyle=!bs!color{blue},
      linewidth=6in,
      numberstyle=!bs!tiny!bs!color{codegray},
      stringstyle=!bs!color{codepurple},
      basicstyle=!bs!footnotesize,
      breakatwhitespace=false,         
      breaklines=true,                 
      captionpos=b,                    
      keepspaces=true,                 
      numbers=left,                    
      numbersep=5pt,                  
      showspaces=false,                
      showstringspaces=false,
      showtabs=false,                  
      tabsize=2
      }
      %.................................................
!bs!begin{lstlisting}[language=python,style=mystyle6]
output(scrinc('HF')+' Output:'+str(adder(10)))
!bs!end{lstlisting}
          """
   elif "HF" in options:
      x="""
!bs!definecolor{codegreen}{rgb}{0,0.6,0}
!bs!definecolor{codegray}{rgb}{0.5,0.5,0.5}
!bs!definecolor{codepurple}{rgb}{0.58,0,0.82}
!bs!definecolor{backcolour}{rgb}{0.95,0.95,0.92}

      !bs!lstdefinestyle{mystyle6}{
      backgroundcolor=!bs!color{codegray},   
      commentstyle=!bs!color{magenta},
      keywordstyle=!bs!color{blue},
      linewidth=6in,
      numberstyle=!bs!tiny!bs!color{codegray},
      stringstyle=!bs!color{codepurple},
      basicstyle=!bs!footnotesize,
      breakatwhitespace=false,         
      breaklines=true,                 
      captionpos=b,                    
      keepspaces=true,                 
      numbers=left,                    
      numbersep=5pt,                  
      showspaces=false,                
      showstringspaces=false,
      showtabs=false,                  
      tabsize=2
      }
      %.................................................
!bs!begin{lstlisting}[language=python,style=mystyle6]
<script=python2.7:action={!!sid=1!!!!LinNoId=1!!}>
output(scrinc('HF')+' Output:'+str(adder(10)))
</script>!bs!end{lstlisting}
          """
   findrep={'!bs!b':'\\b','!bs!n':'\\\\n','!bs!':'\\'}
   for key in findrep:
      x=x.replace(key,findrep[key])
   return(x)


output(scrinc('HF')+' Output:'+str(adder(10)))
