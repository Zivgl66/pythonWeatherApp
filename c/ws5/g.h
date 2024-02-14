#ifndef G_H
#define G_H 1

#ifndef VAR_DECLS
# define _DECL extern
# define _INIT(x)
#else
# define _DECL
# define _INIT(x)  = x
#endif
 _DECL int g_s _INIT(6);
#endif

