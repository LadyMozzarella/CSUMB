import java.text.DecimalFormat;
import java.util.Scanner;

/**
 * Programming Final Project: Final Project
 * School: CSU, Monterey Bay
 * Course: CST 338 Software Design
 * Professor: Jesse Cecil, MS
 *
 * The final project is very open ended. This project follows one of the
 * requirements for the final exam.
 *
 * @author Brittany Mazza
 */
public class FinalProject
{
   /**
    * Run the final project, which is a recipe book.
    *
    * @param args command line arguments, which are not expected
    */
   public static void main(String[] args)
   {
      Scanner keyboard = new Scanner(System.in);
      // Populate the cookbook with 5 recipes.
      Ingredient mud = new Ingredient("mud", 1, "cup");
      Ingredient pieCrust = new Ingredient("pie crust", 1, "");
      Ingredient worms = new Ingredient("worms", 5, "");
      Ingredient butterfinger = new Ingredient("crushed Butterfingers", 3,
            "king size bars");
      Ingredient iceCream = new Ingredient("vanilla ice cream", 1, "tub");
      Ingredient whippedCream = new Ingredient("whipped cream", 16, "oz");

      Recipe mudPie = new Recipe("Mud Pie",
            new Ingredient[] { mud, pieCrust },
            "Place mud in pie crust.");
      Recipe mudPieWithWorms = new Recipe("Mud Pie w/ Worms",
            new Ingredient[] { mud, pieCrust, worms },
            "Place mud in pie crust. Add worms.");
      Recipe butterfingerPie = new Recipe("Butterfinger Pie",
            new Ingredient[] { pieCrust, butterfinger, iceCream, whippedCream },
            "Mix Butterfinger with ice cream. Place in pie crust. Add whipped"
                  + " cream.");
      Recipe justButterfinger = new Recipe("Just Butterfinger",
            new Ingredient[] { butterfinger },
            "Unwrap and enjoy.");
      Recipe pizza = new Recipe();
      pizza.setName("Pizza");
      pizza.setInstructions("Call your local Pizza Hut. Get pizza.");

      Book cookbook = new Book("My Cookbook", "Brittany Mazza");
      cookbook.addPage(mudPie);
      cookbook.addPage(mudPieWithWorms);
      cookbook.addPage(butterfingerPie);
      cookbook.addPage(justButterfinger);
      cookbook.addPage(pizza);

      // Display title and author.
      System.out.println();
      System.out.println(cookbook.getTitle() + "\nby " + cookbook.getAuthor());

      // Display the first page, but allow the user to select previous or
      // next, if available ("done" to exit).
      boolean isDone;
      int page = 1;
      do
      {
         // Display recipe to user.
         Recipe recipe = (Recipe) cookbook.getPage(page);
         System.out.println(recipe.toString());

         // Ask the user what to do next.
         boolean isPrevAvailable = cookbook.getPage(page - 1) != null;
         boolean isNextAvailable = cookbook.getPage(page + 1) != null;
         System.out.println("\nWhat would you like to do?");
         System.out.println(" * \"done\" to quit.");
         if (isPrevAvailable)
            System.out.println(" * \"previous\" to go to previous page.");
         if (isNextAvailable)
            System.out.println(" * \"next\" to go to next page.");

         // Get request from user and handle it appropriately.
         String command = keyboard.next();
         keyboard.nextLine(); // Clear any input still in scanner.
         isDone = command.equals("done") || command.equals("d")
               || command.equals("q");
         if ((command.equals("previous") || command.equals("p"))
               && isPrevAvailable)
            page--;
         if ((command.equals("next") || command.equals("n")) && isNextAvailable)
            page++;
      } while (!isDone);

      keyboard.close();
      // The test method can be added at any moment to ensure that the
      // individual classes themselves still work.
      // test();
   }

   /**
    * A simple method that can easily be run to test the classes that are
    * used for this assignment.
    */
   private static void test()
   {
      // ***********************************************************************
      // Test the methods on the Ingredient class.
      System.out.println("Ingredients:");
      Ingredient bakingPowder = new Ingredient();
      System.out.println(bakingPowder.toString());
      bakingPowder.setName("baking powder");
      bakingPowder.setQuantity(3.5);
      bakingPowder.setUnitType("tsp");
      System.out.println(bakingPowder.toString());

      Ingredient flour = new Ingredient("all-purpose flour" , 1.5, "cup");
      System.out.println(flour.toString());

      Ingredient salt = new Ingredient();
      salt.setName("salt");
      salt.setQuantity(1);
      salt.setUnitType("tsp");
      System.out.println(salt.toString());

      // ***********************************************************************
      // Test the methods on the Recipe class.
      Ingredient whiteSugar = new Ingredient("white sugar", 1, "tbsp");
      Ingredient milk = new Ingredient("milk", 1.25, "cup");
      Ingredient egg = new Ingredient("egg", 1, "");
      Ingredient butter = new Ingredient("melted butter", 3, "tbsp");
      Ingredient[] ingredients = new Ingredient[]{ flour, bakingPowder, salt,
            whiteSugar, milk, egg, butter };
      String instructions = "1. In a large bowl, sift together the flour, "
            + "baking powder, salt and sugar. Make a well in the center and "
            + "pour in the milk, egg and melted butter; mix until smooth.\n"
            + "2. Heat a lightly oiled griddle or frying pan over medium high "
            + "heat. Pour or scoop the batter onto the griddle, using "
            + "approximately 1/4 cup for each pancake. Brown on both sides and "
            + "serve hot.";

      Recipe pancakes1 = new Recipe();
      pancakes1.setPageNumber(1);
      pancakes1.setName("Pancakes #1");
      pancakes1.setIngredients(ingredients);
      pancakes1.setInstructions(instructions);
      System.out.println(pancakes1);

      Recipe pancakes2 = new Recipe("Pancakes #2", ingredients, instructions);
      pancakes2.setPageNumber(2);
      System.out.println(pancakes2);

      Recipe pancakes3 = new Recipe(3, "Pancakes #3", ingredients,
            instructions);
      System.out.println(pancakes3);

      // ***********************************************************************
      // Test the methods on the Book class.
      Book cookbook = new Book("My Cookbook", "Fred Armisen");
      cookbook.addPage(pancakes1);
      cookbook.addPage(pancakes2);
      cookbook.addPage(pancakes3);
      cookbook.removePage(1);
      cookbook.addPage(pancakes3);

      System.out.println("\n\n" + cookbook.getTitle() + "\nby "
            + cookbook.getAuthor());
      for (int i = 1; i <= cookbook.getTotalPages(); i++)
      {
         Recipe recipe = (Recipe) cookbook.getPage(i);
         System.out.println(recipe.toString());
      }
   }
}

/**
 * An ingredient line item for a recipe.
 *
 * @author Brittany Mazza
 */
class Ingredient
{
   private String name;
   private double quantity;
   private String unitType;

   /**
    *
    * Create a new ingredient based on the supplied values.
    *
    * @param name name of the ingredient, like "chopped celery"
    * @param quantity quantity of the ingredient, like "3.5"
    * @param unitType type of the ingredient, like "cups"
    */
   Ingredient(String name, double quantity, String unitType)
   {
      this.name = name;
      this.quantity = quantity;
      this.unitType = unitType;
   }

   /**
    * Create a new ingredient. Defaults values will be used for this call
    * that describe a completely empty ingredient.
    */
   Ingredient()
   {
      name = "";
      quantity = 0;
      unitType = "";
   }

   /**
    * Set the ingredient name.
    *
    * @param name the name of the ingredient, like "chopped celery"
    * @return true if set correctly, false otherwise
    */
   public boolean setName(String name)
   {
      if (name == null)
      {
         return false;
      }
      this.name = name;
      return true;
   }

   /**
    * Set the quantity of the ingredient.
    *
    * @param quantity the amount of the ingredient, like "3.5"
    * @return true if set correctly, false otherwise
    */
   public boolean setQuantity(double quantity)
   {
      this.quantity = quantity;
      return true;
   }

   /**
    * Set the type of unit for the ingredient.
    *
    * @param unitType the unit type for the ingredient, like "cups"
    * @return true if set correctly, false otherwise
    */
   public boolean setUnitType(String unitType)
   {
      if (unitType == null)
      {
         return false;
      }
      this.unitType = unitType;
      return true;
   }

   /**
    * Get the name of the ingredient.
    *
    * @return the name of the ingredient
    */
   public String getName()
   {
      return name;
   }

   /**
    * Get the amount of the ingredient.
    *
    * @return the amount of the ingredient
    */
   public double getQuantity()
   {
      return quantity;
   }

   /**
    * Get the unit type of the ingredient.
    *
    * @return the unit type of the ingredient
    */
   public String getUnitType()
   {
      return unitType;
   }

   /**
    * A String representation of this ingredient.
    *
    * @return a neatly formatted string to display
    */
   @Override
   public String toString()
   {
      DecimalFormat formatter = new DecimalFormat("0.00");
      return String.format("%-50s", name)
            + formatter.format(quantity) + " " + unitType;
   }
}


/**
 * A page in a book.
 */
abstract class Page implements Cloneable
{
   private int number;
   private String content;

   /**
    * Create a new page. Defaults will be set and will need to be manipulated
    * later for all variables.
    */
   Page()
   {
      number = 0;
      content = "";
   }

   /**
    * Set the page number.
    *
    * @param pageNumber the new page number
    * @return true if set correctly, false otherwise
    */
   public boolean setPageNumber(int pageNumber)
   {
      this.number = pageNumber;
      return true;
   }

   /**
    * Set the content of the page.
    *
    * @param content the new page content
    * @return true if set correctly, false otherwise
    */
   public boolean setContent(String content)
   {
      if (content == null)
      {
         return false;
      }
      this.content = content;
      return true;
   }

   /**
    * Get the page number.
    *
    * @return the page number
    */
   public int getNumber()
   {
      return number;
   }

   /**
    * Get the page content.
    *
    * @return the page content
    */
   public String getContent()
   {
      return content;
   }

   /**
    * Get a deep copy of this page.
    *
    * @return a deep copy of page
    * @throws CloneNotSupportedException when a clone can't be produced
    */
   public Page clone() throws CloneNotSupportedException
   {
      return (Page) super.clone();
   }

   /**
    * Get the string representation of the page.
    *
    * @return the page, represented as a string
    */
   @Override
   public String toString()
   {
      return "_________________________________________________________________"
            + "\n" + number + "\n\n" + content;
   }
}

/**
 * A recipe for a cookbook.
 */
class Recipe extends Page
{
   private Ingredient[] ingredients;
   private String instructions;
   private String name;

   /**
    * Create a new recipe with the indicated page number and recipe information.
    *
    * @param number       the page number
    * @param name         the name of the recipe
    * @param ingredients  the ingredients for the recipe
    * @param instructions the instructions for the recipe
    */
   Recipe(int number, String name, Ingredient[] ingredients,
          String instructions)
   {
      this.name = name;
      this.ingredients = ingredients;
      this.instructions = instructions;
      setPageNumber(number);
      updateContent();
   }

   /**
    * Create a new recipe without a defined page number.
    *
    * @param name         the name of the recipe
    * @param ingredients  the ingredients for the recipe
    * @param instructions the instructions for the recipe
    */
   Recipe(String name, Ingredient[] ingredients, String instructions)
   {
      this.name = name;
      this.ingredients = ingredients;
      this.instructions = instructions;
      setPageNumber(0);
      updateContent();
   }

   /**
    * Create a new recipe with all of the default values.
    */
   Recipe()
   {
      name = "";
      ingredients = new Ingredient[0];
      instructions = "";
      setPageNumber(0);
      updateContent();
   }

   /**
    * Set the name of the recipe.
    *
    * @param name the name of the recipe
    *
    * @return true if set correctly, false otherwise
    */
   public boolean setName(String name)
   {
      if (name == null)
      {
         return false;
      }
      this.name = name;
      updateContent();
      return true;
   }

   /**
    * Set the ingredients of the recipe.
    *
    * @param ingredients the ingredients for the recipe
    *
    * @return true if set correctly, false otherwise
    */
   public boolean setIngredients(Ingredient[] ingredients)
   {
      if (ingredients == null)
      {
         return false;
      }
      this.ingredients = ingredients;
      updateContent();
      return true;
   }

   /**
    * Set the instructions for the recipe.
    *
    * @param instructions the instructions for the recipe
    *
    * @return true if set correctly, false otherwise
    */
   public boolean setInstructions(String instructions)
   {
      if (instructions == null)
      {
         return false;
      }
      this.instructions = instructions;
      updateContent();
      return true;
   }

   /**
    * Get the name for the recipe.
    *
    * @return the name for the recipe
    */
   public String getName()
   {
      return name;
   }

   /**
    * Get the ingredients for the recipe.
    *
    * @return the ingredients for the recipe
    */
   public Ingredient[] getIngredients()
   {
      return ingredients;
   }

   /**
    * Get the instructions for the recipe.
    *
    * @return the instructions for the recipe
    */
   public String getInstructions()
   {
      return instructions;
   }

   /**
    * Update the page content based on existing recipe information.
    */
   private void updateContent()
   {
      String content = name + "\n\n";

      for (Ingredient ingredient : ingredients)
      {
         content += ingredient.toString() + "\n";
      }
      content += "\n" + instructions;
      setContent(content);
   }
}

/**
 * A book.
 */
class Book implements Cloneable
{
   public static int MAX_PAGES = 5;
   private String title;
   private String author;
   private Page[] pages;
   private int totalPages;

   /**
    * Create a new book with a title and author.
    *
    * @param title the title of the book
    * @param author the author of the book
    */
   Book(String title, String author)
   {
      this.title = title;
      this.author = author;
      pages = new Page[MAX_PAGES];
      totalPages = 0;
   }

   /**
    * Create a new book.
    */
   Book()
   {
      title = "";
      author = "";
      pages = new Page[MAX_PAGES];
      totalPages = 0;
   }

   /**
    * Set the title of the book.
    *
    * @param title the title of the book
    * @return true if set correctly, false otherwise
    */
   public boolean setTitle(String title)
   {
      if (title == null)
      {
         return false;
      }
      this.title = title;
      return true;
   }

   /**
    * Set the author of the book.
    *
    * @param author the author of the book
    * @return true if set correctly, false otherwise
    */
   public boolean setAuthor(String author)
   {
      if (author == null)
      {
         return false;
      }
      this.author = author;
      return true;
   }

   /**
    * Get the title of the book.
    *
    * @return true if set correctly, false otherwise
    */
   public String getTitle()
   {
      return title;
   }

   /**
    * Get the author of the book.
    *
    * @return true if set correctly, false otherwise
    */
   public String getAuthor()
   {
      return author;
   }

   /**
    * Get the number of total pages in the book.
    *
    * @return the number of total pages
    */
   public int getTotalPages()
   {
      return totalPages;
   }

   /**
    * Get a particular page based on the page number.
    *
    * @param pageNumber the page number to get the page of
    * @return the page at the particular location, null if not a valid page
    */
   public Page getPage(int pageNumber)
   {
      if (pageNumber < 1 || pageNumber > totalPages)
      {
         // Page is not within a valid range and can't be obtained.
         return null;
      }
      return pages[pageNumber - 1];
   }

   /**
    * Add a particular page to this book.
    *
    * @param page the page to add to the book
    * @return true if added correctly, false otherwise
    */
   public boolean addPage(Page page)
   {
      if (page == null || totalPages >= MAX_PAGES)
      {
         return false;
      }
      pages[totalPages] = page;
      totalPages++;
      paginatePages();
      return true;
   }

   /**
    * Remove a particular page from this book.
    *
    * @param pageNumber the page to remove from the book
    * @return the page removed from the book
    */
   public Page removePage(int pageNumber)
   {
      if (pageNumber < 1 || pageNumber > totalPages)
      {
         // Page is not within a valid range and can't be removed.
         return null;
      }
      Page lastPage = pages[totalPages - 1];
      Page removedPage = pages[pageNumber - 1];
      pages[pageNumber - 1] = lastPage;
      pages[totalPages - 1] = null;
      totalPages--;
      paginatePages();
      return removedPage;
   }

   /**
    * Get a deep clone of this book.
    *
    * @return a deep clone of book
    * @throws CloneNotSupportedException when a clone can't be produced
    */
   @Override
   public Book clone() throws CloneNotSupportedException
   {
      Book copy = (Book) super.clone();
      for (int i = 0; i < pages.length; i++)
      {
         copy.pages[i] = pages[i].clone();
      }
      return copy;
   }

   /**
    * Add/reset page numbers for all pages within this book.
    */
   private void paginatePages()
   {
      int pageNumber = 1;
      for (Page page : pages)
      {
         if (page != null)
         {
            page.setPageNumber(pageNumber);
         }
         pageNumber++;
      }
   }
}

/**************** Example Run **************************************************

My Cookbook
by Brittany Mazza
_________________________________________________________________
1

Mud Pie

mud                                               1.00 cup
pie crust                                         1.00

Place mud in pie crust.

What would you like to do?
* "done" to quit.
* "next" to go to next page.
next
_________________________________________________________________
2

Mud Pie w/ Worms

mud                                               1.00 cup
pie crust                                         1.00
worms                                             5.00

Place mud in pie crust. Add worms.

What would you like to do?
* "done" to quit.
* "previous" to go to previous page.
* "next" to go to next page.
next
_________________________________________________________________
3

Butterfinger Pie

pie crust                                         1.00
crushed Butterfingers                             3.00 king size bars
vanilla ice cream                                 1.00 tub
whipped cream                                     16.00 oz

Mix Butterfinger with ice cream. Place in pie crust. Add whipped cream.

What would you like to do?
* "done" to quit.
* "previous" to go to previous page.
* "next" to go to next page.
next
_________________________________________________________________
4

Just Butterfinger

crushed Butterfingers                             3.00 king size bars

Unwrap and enjoy.

What would you like to do?
* "done" to quit.
* "previous" to go to previous page.
* "next" to go to next page.
next
_________________________________________________________________
5

Pizza


Call your local Pizza Hut. Get pizza.

What would you like to do?
* "done" to quit.
* "previous" to go to previous page.
next
_________________________________________________________________
5

Pizza


Call your local Pizza Hut. Get pizza.

What would you like to do?
* "done" to quit.
* "previous" to go to previous page.
previous
_________________________________________________________________
4

Just Butterfinger

crushed Butterfingers                             3.00 king size bars

Unwrap and enjoy.

What would you like to do?
* "done" to quit.
* "previous" to go to previous page.
* "next" to go to next page.
previous
_________________________________________________________________
3

Butterfinger Pie

pie crust                                         1.00
crushed Butterfingers                             3.00 king size bars
vanilla ice cream                                 1.00 tub
whipped cream                                     16.00 oz

Mix Butterfinger with ice cream. Place in pie crust. Add whipped cream.

What would you like to do?
* "done" to quit.
* "previous" to go to previous page.
* "next" to go to next page.
previous
_________________________________________________________________
2

Mud Pie w/ Worms

mud                                               1.00 cup
pie crust                                         1.00
worms                                             5.00

Place mud in pie crust. Add worms.

What would you like to do?
* "done" to quit.
* "previous" to go to previous page.
* "next" to go to next page.
previous
_________________________________________________________________
1

Mud Pie

mud                                               1.00 cup
pie crust                                         1.00

Place mud in pie crust.

What would you like to do?
* "done" to quit.
* "next" to go to next page.
done

Process finished with exit code 0

*******************************************************************************/
