from exector import run, run2
from transpiler import transpile
import math

if __name__ == "__main__":
   # Just testing das'all...
   code = """
         import something;

         # I'm not sure if 'someting.Person' will work...
         Person = something.Person;

         class Man inherits Person {
          has name;
          has has_pp;
          has age;
          has title = 'Mr.';
          has gender = 'male';

          use Person(name);

          def when_created() {
              print("Man was created!")
          };

         };

         frank = Man(name="Frank Abgna", has_pp=True, age=20);

         print(frank.say_hello());
         print(issubclass(Man, Person));

            hello(age=20.3, year=1999);
            dict = {1:2};
            print(dict);
         """

   run2(transpile(code))
