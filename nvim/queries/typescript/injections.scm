;; Extend built-in injections
(call_expression
  function: (non_null_expression
    (instantiation_expression
      (await_expression
        (identifier) @_name)))
  arguments: (template_string) @injection.content
  (#eq? @_name "sql")
  (#set! injection.language "sql")
  (#set! injection.include-children))

;; Handle simpler variants like sql`...` and await sql`...`
(call_expression
  function: [
    (identifier) @_name
    (await_expression (identifier) @_name)
    (instantiation_expression function: (identifier) @_name)
  ]
  arguments: (template_string) @injection.content
  (#eq? @_name "sql")
  (#set! injection.language "sql")
  (#set! injection.include-children))

;; Support tx`...` and tx<User>`...`
(call_expression
  function: (non_null_expression
    (instantiation_expression
      (await_expression
        (identifier) @_name)))
  arguments: (template_string) @injection.content
  (#eq? @_name "tx")
  (#set! injection.language "sql")
  (#set! injection.include-children))

;; Handle simpler variants for tx as well
(call_expression
  function: [
    (identifier) @_name
    (await_expression (identifier) @_name)
    (instantiation_expression function: (identifier) @_name)
  ]
  arguments: (template_string) @injection.content
  (#eq? @_name "tx")
  (#set! injection.language "sql")
  (#set! injection.include-children))
