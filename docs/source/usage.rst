###########################
Usage
###########################

font-size: 

:large:`large`
:larger:`larger`
:x-large:`x-large`
:xx-large:`xx-large`
:small:`small`
:smaller:`smaller`
:x-small:`x-small`
:xx-small:`xx-small`
:medium:`medium`

This is :red:`red !` And :blue:`this part is blue`.


Check out the `Installation`_ section for further information.

Check out the :doc:`usage` section for further information, including how to
:ref:`install <installation>` the project.

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.

.. note:: 

   This is example.


.. cpp:function:: bool myMethod(int arg1, std::string arg2)

   A function with parameters and types.

.. cpp:function:: bool myMethod(int, double)

   A function with unnamed parameters.

.. cpp:function:: const T &MyClass::operator[](std::size_t i) const

   An overload for the indexing operator.

.. cpp:function:: operator bool() const

   A casting operator.

.. cpp:function:: constexpr void foo(std::string &bar[2]) noexcept

   A constexpr function.

.. cpp:function:: MyClass::MyClass(const MyClass&) = default

   A copy constructor with default implementation.

.. js:function:: $.getJSON(href, callback[, errback])

   :param string href: An URI to the location of the resource.
   :param callback: Gets called with the object.
   :param errback:
       Gets called in case the request fails. And a lot of other
       text so we need multiple lines.
   :throws SomeError: For whatever reason in that case.
   :returns: Something.

.. rst:directive:: foo

   Foo description.

.. rst:directive:: .. bar:: baz

   Bar description.

.. index:: single: execution
           single: execution; context

.. sectionauthor:: Guido van Rossum <guido@python.org>
.. codeauthor:: name <email>

.. glossary::

   environment
      A structure where information about all documents under the root is
      saved, and used for cross-referencing.  The environment is pickled
      after the parsing stage, so that successive runs only need to read
      and parse new and changed documents.

   source directory
      The directory which, including its subdirectories, contains all
      source files for one Sphinx project.
.. glossary::

   term 1
   term 2
      Definition of both terms.

.. highlight:: c
.. sourcecode:: c
    :linenos: 
    :emphasize-lines: 3,5
    :lineno-start: 1

    int main(){
        int a;
        int b;
        int c = a + b;
        return c;
    }

.. literalinclude:: Blink.py
    :linenos: 
    :language: python

.. literalinclude:: Blink.py
    :linenos: 
    :language: python
    :pyobject: setup

.. attention::
    Information that requires the reader’s attention. The content of the directive should be written in complete sentences and include all appropriate punctuation.
.. caution::
    Information with regard to which the reader should exercise care. The content of the directive should be written in complete sentences and include all appropriate punctuation.

Since Pythagoras, we know that :math:`a^2 + b^2 = c^2`.

By default, inline code such as :code:`1 + 2` just displays without
highlighting.

.. This is a comment.

..
   This whole indented block
   is a comment.

   Still in the comment.


This is a paragraph that contains `a link`_.

.. _a link: https://domain.invalid/

`Link text <https://domain.invalid/>`_

=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+

* This is a bulleted list.
* It has two items, the second
  item uses two lines.

1. This is a numbered list.
2. It has two items too.

#. This is a numbered list.
#. It has two items too.

* this is
* a list

  * with a nested list
  * and some subitems

* and here the parent list continues

term (up to a line of text)
   Definition of the term, which must be indented

   and can even consist of multiple paragraphs

next term
   Description.

| These lines are
| broken exactly like in
| the source file.

This is a normal text paragraph. The next paragraph is a code sample::

   It is not processed in any way, except
   that the indentation is removed.

   It can span multiple lines.

This is a normal text paragraph again.


To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache


.. _installation:

Installation
------------

...


Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. py:function:: lumache.get_random_ingredients(kind=None)

   Return a list of random ingredients as strings.

   :param kind: Optional "kind" of ingredients.
   :type kind: list[str] or None
   :return: The ingredients list.
   :rtype: list[str]



The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. py:function:: lumache.get_random_ingredients(kind=None)

   Return a list of random ingredients as strings.

   :param kind: Optional "kind" of ingredients.
   :type kind: list[str] or None
   :raise lumache.InvalidKindError: If the kind is invalid.
   :return: The ingredients list.
   :rtype: list[str]


>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']