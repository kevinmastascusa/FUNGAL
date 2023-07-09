# Required Libraries
library(shiny)
library(ggplot2)
library(qqman) # for manhattan plots

# Function to generate random GWAS data
generate_gwas_data <- function(n) {
  data.frame(
    SNP = paste0("rs", seq(n)),
    chromosome = sample(1:22, n, replace = TRUE), # change to numeric
    bp = sample(1:1e6, n, replace = TRUE),
    p = runif(n, min = 0, max = 1)
  )
}

# Define UI
ui <- fluidPage(
  titlePanel("Genomics Explorer - GWAS"),
  
  sidebarLayout(
    sidebarPanel(
      sliderInput("num_points", "Number of SNPs:", 
                  min = 1, max = 5000, value = 1000)
    ),
    
    mainPanel(
      plotOutput("manhattan_plot")
    )
  )
)

# Define Server Logic
server <- function(input, output) {
  
  data <- reactive({
    generate_gwas_data(input$num_points)
  })
  
  output$manhattan_plot <- renderPlot({
    manhattan(data(),
              chr = "chromosome", bp = "bp", p = "p",
              main = "Manhattan Plot of GWAS P-Values",
              ylim = c(0, -log10(min(data()$p))))
  })
}

# Run the Application
shinyApp(ui = ui, server = server)
