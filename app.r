library(shiny)
library(ggplot2)

# Set up the dimensions of the grid
grid_width <- 40
grid_height <- 30
cell_size <- 10
num_cols <- grid_width / cell_size
num_rows <- grid_height / cell_size

# Initialize the grid with random cell states
grid <- matrix(sample(c(0, 1), num_cols * num_rows, replace = TRUE, prob = c(0.2, 0.8)), nrow = num_rows, ncol = num_cols)

# Define the Shiny UI
ui <- fluidPage(
  titlePanel("Game of Life"),
  sidebarLayout(
    sidebarPanel(
      sliderInput("speed", "Speed", min = 1, max = 10, value = 5),
      actionButton("start_stop", "Start/Stop"),
      actionButton("reset", "Reset")
    ),
    mainPanel(
      plotOutput("grid_plot", width = "400px", height = "300px")
    )
  )
)

# Define the Shiny server
server <- function(input, output, session) {
  # Set up reactive values
  state <- reactiveValues(grid = grid, running = FALSE)
  
  # Function to update the grid
  updateGrid <- function() {
    new_grid <- state$grid
    for (row in 1:num_rows) {
      for (col in 1:num_cols) {
        cell_state <- state$grid[row, col]
        num_neighbors <- sum(state$grid[max(1, row-1):min(row+1, num_rows), max(1, col-1):min(col+1, num_cols)])
        
        # Apply the rules of the Game of Life
        if (cell_state == 0 && num_neighbors == 3) {
          new_grid[row, col] <- 1
        } else if (cell_state == 1 && (num_neighbors < 2 || num_neighbors > 3)) {
          new_grid[row, col] <- 0
        }
      }
    }
    state$grid <- new_grid
  }
  
  # Define the grid plot
  output$grid_plot <- renderPlot({
    grid_data <- data.frame(x = rep(1:num_cols, num_rows), y = rep(num_rows:1, each = num_cols), state = as.vector(state$grid))
    
    ggplot(grid_data, aes(x = x, y = y, fill = factor(state))) +
      geom_tile(color = "white", width = 0.9, height = 0.9) +
      scale_fill_manual(values = c("white", "black")) +
      coord_equal() +
      theme_void() +
      theme(panel.background = element_rect(fill = "white"),
            axis.text = element_blank(),
            axis.title = element_blank(),
            axis.ticks = element_blank(),
            panel.grid = element_blank())
  })
  
  # Start/Stop button
  observeEvent(input$start_stop, {
    if (state$running) {
      state$running <- FALSE
    } else {
      state$running <- TRUE
      observe({
        invalidateLater(input$speed * 1000)
        updateGrid()
      })
    }
  })
  
  # Reset button
  observeEvent(input$reset, {
    state$grid <- matrix(sample(c(0, 1), num_cols * num_rows, replace = TRUE, prob = c(0.2, 0.8)), nrow = num_rows, ncol = num_cols)
    state$running <- FALSE
  })
}

# Run the Shiny app
shinyApp(ui, server)
