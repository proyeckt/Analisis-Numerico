#SIMULACIÓN MODELO SIR - COVID-19 BRASIL

#Edwin Turizo Prieto
#Juan Camilo Pimienta


library(readxl)
library(phaseR)
library(deSolve)
library(shiny)
library(shinydashboard)

MAX_ROWS=78;
DatosBrasil <- read_excel("covid_br.xlsx", 
                      sheet = "Sheet 1",na="0")



# Define UI for application that draws a histogram
ui <- fluidPage(
  
  tags$head(tags$style(
    HTML('
             .well {
                background-color: #ccc;
            }
    
            body, label, input, button, select { 
              font-family: "italic";
            }')
  )),
  
  
  titlePanel("SIMULACIÓN MODELO SIR - COVID-19 BRASIL"),
  
  sidebarLayout(
      sliderInput("gamma",
                  "Variación de valor gamma:",
                  min = 0,
                  max = 1,
                  value = 0.5,
                  step=0.0001),
      sliderInput("beta",
                  "Variación de valor beta:",
                  min = 0,
                  max = 3,
                  value = 1.5,
                  step=0.0001),
    ),
  numericInput("nPoblacion", "Numero de Población", 0),
  numericInput("nDias", "Numero de Dias", 0),
  numericInput("nInfectadosInicial", "Numero Inicial de Infectados", 0),
  actionButton("btnRK4", "Generar SIR Runge Kutta 4"),
  actionButton("btnAdams", "Generar SIR Adams"),
  textOutput("poblacion"),
  mainPanel(
    plotOutput("sirRk4"),
    plotOutput("sirAdams"),
    plotOutput("erroresRk4S"),
    plotOutput("erroresRk4I"),
    plotOutput("erroresRk4R"),
    plotOutput("erroresAdamsS"),
    plotOutput("erroresAdamsI"),
    plotOutput("erroresAdamsR")
  )
  )

server <- function(input, output) {
  sir <- function(time, state, parameters) {
    with(as.list(c(state, parameters)), {
      
      dS <- -beta * S * I
      dI <- beta * S * I - gamma * I
      dR <- gamma * I
      return(list(c(dS, dI, dR)))
    })
  }
  recup=as.numeric(unlist(DatosBrasil[1,12]))
  if(is.na(recup))
    recup=0;
  observeEvent(input$btnRK4, {
    #output$poblacion <- renderText(recup)
    output$sirRk4 <- renderPlot({
      init       <- c(S = 1-(input$nInfectadosInicial/input$nPoblacion)-(recup/input$nPoblacion), I = input$nInfectadosInicial/input$nPoblacion, R = (recup/input$nPoblacion))
      #init       <- c(S = 1-0.00172249, I = 0.00172249, R = 0 )
      parameters <- c(beta = input$beta, gamma = input$gamma)
      #init       <- c(S = 1-1e-6, I = 1e-6, R = 0.0)
      ## beta: infection parameter; gamma: recovery parameter
      #parameters <- c(beta = 1.4247, gamma = 0.14286)
      ## Time frame
      times      <- seq(0, input$nDias, by = 1)
      
      ## Solve using ode (General Solver for Ordinary Differential Equations)
      out <- ode(y = init, times = times, func = sir, parms = parameters, method="rk4")
      ## change to data frame
      out <- as.data.frame(out)
      ## Delete time variable
      out$time <- NULL
      ## Show data
      head(out, 30)
      R_susceptibles=c(as.numeric(unlist(out[1])))
      R_infectados=c(as.numeric(unlist(out[2])))
      R_recuperados=c(as.numeric(unlist(out[3])))
      ## Plot
      matplot(x = times, y = out, type = "l",
              xlab = "Tiempo (Dias)", ylab="Población", main = "SIR con RK4",
              lwd = 1, lty = 1, bty = "l", col = 2:4)
      
      ## Add legend
      legend(40, 0.7, c("Susceptibles", "Infectados", "Recuperados"), pch = 1, col = 2:4, bty = "n")
      
      nRK4=min(c(MAX_ROWS,length(R_susceptibles)))
      
      erroresAbsolutosS=c();
      erroresRelativosS=c();
      erroresAbsolutosI=c();
      erroresRelativosI=c();
      erroresAbsolutosR=c();
      erroresRelativosR=c();
      for(i in 1:nRK4){
        recup=as.numeric(unlist(DatosBrasil[i,13]))
        if(is.na(recup))
          recup=0;
        #S
        nSusceptibles= 1-(as.numeric(unlist(DatosBrasil[i,11]))/input$nPoblacion)-(recup/input$nPoblacion)
        erroresAbsolutosS[i]=abs(R_susceptibles[i]-nSusceptibles)
        erroresRelativosS[i]=erroresAbsolutosS[i]/abs(nSusceptibles)
        #I
        nInfectados= (as.numeric(unlist(DatosBrasil[i,11]))/input$nPoblacion)
        erroresAbsolutosI[i]=abs(R_infectados[i]-nInfectados)
        erroresRelativosI[i]=erroresAbsolutosI[i]/abs(nInfectados)
        #R
        nRecuperados=(recup/input$nPoblacion)
        erroresAbsolutosR[i]=abs(R_recuperados[i]-nRecuperados)
        erroresRelativosR[i]=erroresAbsolutosR[i]/abs(nRecuperados)
      }
      new_times<- seq(1, nRK4, by = 1)
      output$erroresRk4S <- renderPlot({
        matplot(x = new_times, y = erroresAbsolutosS, type = "l",
                xlab = "Tiempo (Dias)", ylab="Error", main = "Errores Susceptibles RK4",
                lwd = 1, lty = 1, bty = "l", col = 2:3)
      })
      output$erroresRk4I <- renderPlot({
        matplot(x = new_times, y = erroresAbsolutosI, type = "l",
                xlab = "Tiempo (Dias)", ylab="Error", main = "Errores Infectados RK4",
                lwd = 1, lty = 1, bty = "l", col = 2:3)
      })
      output$erroresRk4R <- renderPlot({
        matplot(x = new_times, y = erroresAbsolutosR, type = "l",
                xlab = "Tiempo (Dias)", ylab="Error", main = "Errores Recuperados RK4",
                lwd = 1, lty = 1, bty = "l", col = 2:3)
      })
  })

  })
  observeEvent(input$btnAdams, {
    #output$poblacion <- renderText(recup)
    output$sirAdams <- renderPlot({
      init       <- c(S = 1-(input$nInfectadosInicial/input$nPoblacion)-(recup/input$nPoblacion), I = input$nInfectadosInicial/input$nPoblacion, R = (recup/input$nPoblacion))
      parameters <- c(beta = input$beta, gamma = input$gamma)
      
      times      <- seq(1, input$nDias, by = 1)
      
      out <- ode(y = init, times = times, func = sir, parms = parameters, method="adams")
      out <- as.data.frame(out)
      out$time <- NULL
      head(out, 30)
      A_susceptibles=c(as.numeric(unlist(out[1])))
      A_infectados=c(as.numeric(unlist(out[2])))
      A_recuperados=c(as.numeric(unlist(out[3])))
      
      ## Plot
      matplot(x = times, y = out, type = "l",
              xlab = "Tiempo (Dias)", ylab="Población", main = "SIR con Adams",
              lwd = 1, lty = 1, bty = "l", col = 2:4)
      
      ## Add legend
      legend(40, 0.7, c("Susceptibles", "Infectados", "Recuperados"), pch = 1, col = 2:4, bty = "n")
      
      nAdams=min(c(MAX_ROWS,length(A_susceptibles)))
      
      erroresAbsolutosS=c();
      erroresRelativosS=c();
      erroresAbsolutosI=c();
      erroresRelativosI=c();
      erroresAbsolutosR=c();
      erroresRelativosR=c();
      nSusceptibles=0
      for(i in 1:nAdams ){
        recup=as.numeric(unlist(DatosBrasil[i,13]))
        if(is.na(recup))
          recup=0;
        #S
        nSusceptibles= 1-(as.numeric(unlist(DatosBrasil[i,11]))/input$nPoblacion)-(recup/input$nPoblacion)
        erroresAbsolutosS[i]=abs(A_susceptibles[i]-nSusceptibles)
        erroresRelativosS[i]=erroresAbsolutosS[i]/abs(nSusceptibles)
        #I
        nInfectados= (as.numeric(unlist(DatosBrasil[i,11]))/input$nPoblacion)
        erroresAbsolutosI[i]=abs(A_infectados[i]-nInfectados)
        erroresRelativosI[i]=erroresAbsolutosI[i]/abs(nInfectados)
        #R
        nRecuperados=(recup/input$nPoblacion)
        erroresAbsolutosR[i]=abs(A_recuperados[i]-nRecuperados)
        erroresRelativosR[i]=erroresAbsolutosR[i]/abs(nRecuperados)
      }
      new_times<- seq(1, nAdams, by = 1)
      #output$poblacion <- renderText(erroresRelativos)
      output$erroresAdamsS <- renderPlot({
        matplot(x = new_times, y = erroresAbsolutosS, type = "l",
                xlab = "Tiempo (Dias)", ylab="Error", main = "Errores Susceptibles Adams",
                lwd = 1, lty = 1, bty = "l", col = 2:3)
      })
      output$erroresAdamsI <- renderPlot({
        matplot(x = new_times, y = erroresAbsolutosI, type = "l",
                xlab = "Tiempo (Dias)", ylab="Error", main = "Errores Infectados Adams",
                lwd = 1, lty = 1, bty = "l", col = 2:3)
      })
      output$erroresAdamsR <- renderPlot({
        matplot(x = new_times, y = erroresAbsolutosR, type = "l",
                xlab = "Tiempo (Dias)", ylab="Error", main = "Errores Recuperados Adams",
                lwd = 1, lty = 1, bty = "l", col = 2:3)
      })
    })
    
  })
  
}

# Run the application 
shinyApp(ui = ui, server = server)