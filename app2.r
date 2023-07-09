# Required Libraries
library(shiny)
library(ggplot2)

# Function to generate random CpG Island data
generate_cpg_data <- function() {
  data.frame(
    chromosome = paste0("chr", sample(1:22, 100, replace = TRUE)),
    start = sample(1:1e6, 100, replace = TRUE),
    end = sample(1:1e6, 100, replace = TRUE),
    gene = paste0("Gene", sample(LETTERS, 100, replace = TRUE)),
    cpg_density = runif(100)
  )
}

# Define UI
ui <- fluidPage(
  titlePanel("CpG Islands Explorer"),
  
  sidebarLayout(
    sidebarPanel(
      actionButton("generate", "Generate New Data")
    ),
    
    mainPanel(
      plotOutput("plot")
    )
  )
)

# Define Server Logic
server <- function(input, output) {
  data <- eventReactive(input$generate, {
    generate_cpg_data()
  })
  
  output$plot <- renderPlot({
    ggplot(data(), aes(x = start, y = end, color = cpg_density)) +
      geom_point() +
      scale_color_gradient(low = "blue", high = "red") +
      facet_wrap(~ chromosome) +
      theme_minimal() +
      labs(title = "CpG Islands", x = "Start Position", y = "End Position", color = "CpG Density")
  })
}

# Run the Application
shinyApp(ui = ui, server = server)
