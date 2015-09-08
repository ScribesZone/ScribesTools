--- SOIL ---------------------------------------------------------------
-- see http://useocl.sourceforge.net/w/index.php/SOIL

--  Object creation
--  v := new c [(nameExpr)]
-- new c [(nameExpr)]     -- create an object like c1, c2 (uppercase...)
--  create v1,...,vn:c

--  Link object creation (association class)
--  v := new c [(nameExpr)] between (participant1,participant2,...)
--  create v1 : c between (participant1, participant2, ...)

--  Object destruction
--  destroy e

--  Link creation
--  insert (e1; ... ; en) into a j

--  Link destruction
--  delete (e1; ... ; en) from a j

--  Attribut assignement
--  e1.a := e2

--  Variable assignment
--  v := e

-- Operation call
-- [v :=} e1.op(e2; ... ; en)

-- Block of statement
-- [begin] s1; ... ; sn [end]

-- [declare v1 : t1; ... ; vn : tn]

-- if e then s1 [else s2] end
-- for v in e do s end


-- Write('Enter your name: ')
-- aName := ReadLine()
-- Write('Enter your age:')
-- aAge := ReadInteger()
-- Write('Enter your name:')
-- WriteLine('Hello ' + aName + '!')



