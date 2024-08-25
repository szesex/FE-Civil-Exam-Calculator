# FE-Civil-Exam-Calculator
FE Civil Exam Calculator
import numpy as np
import statistics as stats
from scipy.stats import norm

class MathematicsStatistics:
    # Existing methods omitted for brevity

    @staticmethod
    def confidence_interval(mean, z, std_dev, n):
        """Calculate the confidence interval given the mean, z-value, standard deviation, and sample size."""
        margin_of_error = z * (std_dev / np.sqrt(n))
        lower_bound = mean - margin_of_error
        upper_bound = mean + margin_of_error
        return lower_bound, upper_bound

    @staticmethod
    def z_test(sample_mean, population_mean, population_std_dev, n):
        """Perform a Z-test given the sample mean, population mean, population standard deviation, and sample size."""
        z_value = (sample_mean - population_mean) / (population_std_dev / np.sqrt(n))
        return z_value

# Main Program (Extended with Calculation Loop)
def main():
    print("Welcome to the FE Civil Exam Calculator")

    while True:
        print("\nSelect a module:")
        print("1. Mathematics and Statistics")
        print("2. Engineering Economics")
        print("3. Statics")
        print("4. Mechanics of Materials")
        print("5. Fluid Mechanics")
        print("6. Surveying")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            while True:
                print("\nMathematics and Statistics")
                print("1. Distance Between Points")
                print("2. Line Equation")
                print("3. Derivative")
                print("4. Definite Integral")
                print("5. Vector Magnitude")
                print("6. Vector Dot Product")
                print("7. Vector Cross Product")
                print("8. Mean")
                print("9. Standard Deviation")
                print("10. Linear Regression")
                print("11. Polynomial Regression")
                print("12. Exponential Regression")
                print("13. Partial Derivative")
                print("14. Double Integral")
                print("15. Vector Projection")
                print("16. Angle Between Vectors")
                print("17. Confidence Interval")
                print("18. Hypothesis Test (Z-Test)")
                print("0. Back to main menu")

                math_choice = int(input("Select a calculation: "))

                if math_choice == 0:
                    break  # Break the loop and go back to the main menu

                elif math_choice == 17:
                    mean = float(input("Enter the sample mean: "))
                    z = float(input("Enter the z-value (confidence level value): "))
                    std_dev = float(input("Enter the sample standard deviation: "))
                    n = int(input("Enter the sample size: "))
                    lower, upper = MathematicsStatistics.confidence_interval(mean, z, std_dev, n)
                    print(f"Confidence Interval: ({lower}, {upper})")

                elif math_choice == 18:
                    sample_mean = float(input("Enter the sample mean: "))
                    population_mean = float(input("Enter the population mean: "))
                    population_std_dev = float(input("Enter the population standard deviation: "))
                    n = int(input("Enter the sample size: "))
                    z_value = MathematicsStatistics.z_test(sample_mean, population_mean, population_std_dev, n)
                    print(f"Z-Test Value: {z_value}")

                else:
                    print("Feature not implemented yet or invalid choice. Please choose another option.")

        elif choice == 0:
            print("Exiting the program.")
            break  # Exit the main program loop

        else:
            print("Feature not implemented yet or invalid choice. Please choose another module.")

if __name__ == "__main__":
    main()
